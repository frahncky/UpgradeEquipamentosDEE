#!/usr/bin/env python3
"""Confere a coerência entre a base de contatos e as planilhas de prospecção.

Os mesmos 60 registros aparecem em três lugares — empresas/contatos_brasil.tex,
prospeccao/ranking_60_empresas.csv e prospeccao/crm_prospeccao.csv — e os nomes
das empresas são escritos de formas diferentes em cada um. A coluna `Chave` liga
as três fontes; este script usa essa chave para acusar divergência antes que ela
vire ofício enviado com o dado errado.

Uso: python3 ferramentas/verifica_consistencia.py   (0 = tudo certo, 1 = falhas)
"""

import csv
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = RAIZ / "empresas" / "contatos_brasil.tex"
RANKING = RAIZ / "prospeccao" / "ranking_60_empresas.csv"
CRM = RAIZ / "prospeccao" / "crm_prospeccao.csv"
MATRIZ = RAIZ / "laboratorios" / "matriz_laboratorio_empresa.csv"
PRIORIDADES = RAIZ / "laboratorios" / "prioridades_modernizacao.csv"
INDICADORES = RAIZ / "laboratorios" / "levantamento_indicadores_dee.csv"
CADASTRO_LABS = RAIZ / "laboratorios" / "cadastro_laboratorios_dee.csv"

REGISTRO = re.compile(
    r"^\\ContatoEmpresa\n"
    r"  \{(?P<chave>.*?)\}\n"
    r"  \{(?P<empresa>.*?)\}\n"
    r"  \{(?P<nivel>.*?)\}\n",
    re.M,
)
NIVEIS = {"P1", "P2", "P3"}
# Ondas já em prospecção: cada empresa delas precisa do anexo técnico.
ONDAS_COM_ANEXO = {"Onda 1", "Onda 2"}

falhas: list[str] = []


def falha(msg: str) -> None:
    falhas.append(msg)


def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def conferir_colunas(caminho: Path) -> None:
    """Toda linha precisa ter o mesmo número de campos do cabeçalho.

    Vírgula sem aspas num campo de texto já quebrou este repositório antes.
    """
    with caminho.open(encoding="utf-8", newline="") as f:
        linhas = list(csv.reader(f))
    esperado = len(linhas[0])
    for n, linha in enumerate(linhas[1:], start=2):
        if len(linha) != esperado:
            falha(
                f"{caminho.relative_to(RAIZ)}:{n}: {len(linha)} campos, "
                f"esperados {esperado} (vírgula sem aspas?)"
            )


def conferir_esquema_csv(caminho: Path, obrigatorias: tuple[str, ...]) -> list[dict]:
    """Confere a forma e devolve os registros de uma planilha auxiliar."""
    conferir_colunas(caminho)
    linhas = ler_csv(caminho)
    cabecalho = linhas[0].keys() if linhas else ()
    ausentes = [coluna for coluna in obrigatorias if coluna not in cabecalho]
    if ausentes:
        falha(
            f"{caminho.relative_to(RAIZ)}: coluna(s) {ausentes} "
            "ausente(s) no cabeçalho"
        )
    return linhas


def main() -> int:
    blocos = [m.groupdict() for m in REGISTRO.finditer(BASE.read_text(encoding="utf-8"))]
    if not blocos:
        falha(f"{BASE.relative_to(RAIZ)}: nenhum registro \\ContatoEmpresa reconhecido")
        print("\n".join(falhas), file=sys.stderr)
        return 1

    # Chave repetida — de um merge que reintroduz um registro, por exemplo — não
    # pode virar só a última ocorrência: o LaTeX acrescenta as duas à lista e o
    # diretório sai com a empresa duplicada e o resumo por prioridade inflado.
    registros: dict[str, dict] = {}
    for bloco in blocos:
        chave = bloco["chave"]
        if chave in registros:
            falha(f"{BASE.relative_to(RAIZ)}: chave '{chave}' cadastrada mais de uma vez")
        registros[chave] = bloco

    for chave, reg in registros.items():
        if reg["nivel"] not in NIVEIS:
            falha(f"{chave}: nível '{reg['nivel']}' fora de {sorted(NIVEIS)}")
        if not (RAIZ / "empresas" / f"{chave}.tex").is_file():
            falha(f"{chave}: registro sem o ofício empresas/{chave}.tex")

    oficios = {p.stem for p in (RAIZ / "empresas").glob("[0-9]*.tex")}
    for chave in sorted(oficios - set(registros)):
        falha(f"empresas/{chave}.tex: ofício sem registro na base de contatos")

    # As passagens que cruzam arquivos indexam colunas direto. Se um cabeçalho
    # estiver incompleto, elas quebrariam com KeyError e o usuário veria um
    # traceback no lugar do diagnóstico — então o cabeçalho é pré-requisito.
    esquema_ok = True

    for caminho, coluna in ((RANKING, "Prioridade atual"), (CRM, "Prioridade")):
        conferir_colunas(caminho)
        nome = caminho.relative_to(RAIZ)
        linhas = ler_csv(caminho)
        vistas: set[str] = set()

        obrigatorias = ("Chave", "Empresa", "Rank", "Onda", coluna)
        ausentes = [c for c in obrigatorias if linhas and c not in linhas[0]]
        if ausentes:
            falha(f"{nome}: coluna(s) {ausentes} ausente(s) no cabeçalho")
            esquema_ok = False
            continue

        for n, linha in enumerate(linhas, start=2):
            chave = linha["Chave"]
            if chave in vistas:
                falha(f"{nome}:{n}: chave '{chave}' repetida")
            vistas.add(chave)

            registro = registros.get(chave)
            if registro is None:
                falha(f"{nome}:{n}: chave '{chave}' não existe na base de contatos")
                continue
            if linha[coluna] != registro["nivel"]:
                falha(
                    f"{nome}:{n}: {linha['Empresa']} está {linha[coluna]} na planilha "
                    f"e {registro['nivel']} na base"
                )

        for chave in sorted(set(registros) - vistas):
            falha(f"{nome}: empresa '{chave}' da base não aparece na planilha")

    if esquema_ok:
        ranking = {l["Chave"]: l for l in ler_csv(RANKING)}
        for n, linha in enumerate(ler_csv(CRM), start=2):
            alvo = ranking.get(linha["Chave"])
            if alvo is None:
                continue
            for campo in ("Rank", "Empresa", "Onda"):
                if linha[campo] != alvo[campo]:
                    falha(
                        f"crm_prospeccao.csv:{n}: {campo} '{linha[campo]}' difere de "
                        f"'{alvo[campo]}' no ranking"
                    )

    conferir_colunas(MATRIZ)

    prioridades = conferir_esquema_csv(
        PRIORIDADES,
        ("Etapa", "Prioridade", "Laboratório/Eixo", "Orçamento", "Status"),
    )
    niveis_prioridade = {"Máxima", "Alta", "Estratégica"}
    for n, linha in enumerate(prioridades, start=2):
        if linha.get("Prioridade") not in niveis_prioridade:
            falha(
                f"{PRIORIDADES.relative_to(RAIZ)}:{n}: prioridade "
                f"'{linha.get('Prioridade')}' fora de {sorted(niveis_prioridade)}"
            )
        if not linha.get("Laboratório/Eixo"):
            falha(f"{PRIORIDADES.relative_to(RAIZ)}:{n}: laboratório/eixo vazio")
        if not linha.get("Orçamento"):
            falha(f"{PRIORIDADES.relative_to(RAIZ)}:{n}: orçamento sem valor ou marcação")

    indicadores = conferir_esquema_csv(
        INDICADORES,
        ("Indicador", "Período", "Valor", "Unidade", "Fonte interna", "Status"),
    )
    for n, linha in enumerate(indicadores, start=2):
        if not linha.get("Indicador") or not linha.get("Status"):
            falha(f"{INDICADORES.relative_to(RAIZ)}:{n}: indicador ou status vazio")

    laboratorios = conferir_esquema_csv(
        CADASTRO_LABS,
        ("Nome do laboratório", "Macroárea", "Principais usos", "Status de conferência"),
    )
    nomes_labs: set[str] = set()
    for n, linha in enumerate(laboratorios, start=2):
        nome = linha.get("Nome do laboratório", "")
        if not nome:
            falha(f"{CADASTRO_LABS.relative_to(RAIZ)}:{n}: nome do laboratório vazio")
        elif nome in nomes_labs:
            falha(f"{CADASTRO_LABS.relative_to(RAIZ)}:{n}: laboratório '{nome}' repetido")
        nomes_labs.add(nome)

    # Cobertura dos anexos técnicos. O pacote de envio é ofício + dossiê + anexo,
    # então toda empresa das ondas já em campo precisa do seu. O nome do arquivo
    # do anexo é o mesmo do ofício, o que torna o par evidente na hora de montar
    # o pacote — e verificável aqui.
    anexos = {p.stem for p in (RAIZ / "anexos").glob("[0-9]*.md")}
    for chave in sorted(anexos - set(registros)):
        falha(f"anexos/{chave}.md: anexo sem empresa correspondente na base")

    if esquema_ok:
        for linha in ler_csv(RANKING):
            chave, onda = linha["Chave"], linha["Onda"]
            if onda in ONDAS_COM_ANEXO and chave not in anexos:
                falha(f"{linha['Empresa']} ({onda}) está sem o anexo técnico anexos/{chave}.md")

    if falhas:
        print(f"{len(falhas)} divergência(s):", file=sys.stderr)
        for f in falhas:
            print(f"  {f}", file=sys.stderr)
        return 1

    print(f"OK: {len(registros)} empresas coerentes entre a base, o ranking e o CRM.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
