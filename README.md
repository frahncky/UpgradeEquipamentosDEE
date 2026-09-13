# Upgrade de Equipamentos do DEE/IFMA

Repositório de prospecção, formalização e acompanhamento de doações e parcerias para a modernização dos laboratórios do Departamento de Eletroeletrônica (DEE) do IFMA - Campus São Luís/Monte Castelo.

## Visão geral

O projeto deixou de ser apenas uma coleção de ofícios e passou a funcionar como um **sistema completo de captação**. A base atual possui **60 empresas**, contatos brasileiros centralizados, ranking, ondas de prospecção, dossiê institucional, anexos técnicos, matriz por laboratório, CRM e calendário de follow-up.

## Estrutura

### `modelos/`
Documentos institucionais em LaTeX:
- `01_projeto_mae.tex` - programa geral atualizado;
- `02_solicitacao_suap.tex` - solicitação interna;
- `03_oficio_empresa.tex` - modelo genérico;
- `04_manifestacao_interesse.tex` - manifestação preliminar;
- `05_plano_equipamentos.tex` - plano técnico com Top 10 e critérios de ranking;
- `06_relatorio_recebimento.tex` - recebimento e patrimônio;
- `07_checklist_procedimento.tex` - fluxo administrativo.

### `empresas/`
- 60 ofícios individualizados;
- `base_empresa.tex` - corpo comum;
- `contatos_brasil.tex` - fonte única dos dados de prospecção das 60 empresas: prioridade, estratégia, situação, setor prioritário e canal brasileiro;
- `diretorio_contatos.tex` - diretório interno, em PDF, de toda a base (não deve ser enviado às empresas).

### `dossie/`
- `01_dossie_institucional.tex` - dossiê institucional do DEE em LaTeX;
- `02_contrapartidas_institucionais.md` - contrapartidas possíveis e limites;
- `corpo_docente.tex` - distribuição do corpo docente por macroárea;
- `cenario_maranhao.tex` - contexto econômico, industrial, logístico e energético do Maranhão;
- `fontes_cenario_maranhao.md` - fontes oficiais dos indicadores regionais;
- `fluxo_laboratorios.tex` - fluxo em blocos da estrutura laboratorial.
- `03_resumo_executivo.tex` - síntese de uma página para apresentação inicial a gestores e empresas;
- `03_plano_sustentabilidade.md` - governança, segurança, manutenção, capacitação e monitoramento dos recursos.

O dossiê é apresentado **sem fotografias**: a infraestrutura é descrita pelo fluxo em blocos.

### `laboratorios/`
- matriz Laboratório x Empresa x Equipamento;
- plano de modernização por eixo, com níveis Ideal/Intermediário/Mínimo.
- prioridades propostas por etapa, sem valores financeiros inventados;
- cadastro nominal dos laboratórios com pendências de conferência identificadas;
- base para levantamento de indicadores acadêmicos, operacionais e de resultados.

### `prospeccao/`
- ranking das 60 empresas;
- Top 10 do primeiro ciclo;
- CRM de acompanhamento;
- calendário de follow-up;
- pacote padrão de envio;
- composição dos pacotes direcionados às empresas prioritárias;
- modelos de e-mail;
- fontes de priorização.

### `anexos/`
Anexos técnicos das 36 empresas das Ondas 1 e 2, todos com três níveis de solicitação (Ideal/Intermediário/Mínimo). O arquivo tem o mesmo nome do ofício correspondente.

## Top 10 - primeira onda
1. Schneider Electric
2. Equatorial Energia
3. Vale
4. Schweitzer Engineering Laboratories (SEL)
5. WEG
6. Eneva
7. Alcoa/Alumar
8. Altus
9. Intelbras
10. Siemens

O ranking é **interno e preliminar**. Não representa probabilidade estatística de doação.

## Compilação

Todos os documentos usam caminhos relativos à raiz do repositório (`\input{modelos/preambulo.tex}`), portanto **a compilação deve ser feita a partir desta pasta**, com **pdfLaTeX**:

```bash
make              # todos os PDFs em build/
make oficios      # somente os 60 ofícios
make dossie       # somente o dossiê institucional
make diretorio    # somente o diretório interno de contatos
make verificar    # confere a coerência entre a base de contatos e as planilhas
make clean
```

A compilação e a verificação também rodam no CI (`.github/workflows/documentos.yml`) a cada pull request: um job compila os 70 documentos e publica os PDFs, outro roda a conferência de coerência.

Sem `make`, compile um documento individualmente (duas passagens, por causa do sumário e do `\pageref{LastPage}`):

```bash
pdflatex empresas/01_schneider_electric.tex
pdflatex empresas/01_schneider_electric.tex
```

No Overleaf, selecione o arquivo desejado como **Main document** e use o compilador **pdfLaTeX**.

## Contatos no Brasil

`empresas/contatos_brasil.tex` centraliza, em um registro por empresa, a prioridade, a estratégia de abordagem, o setor prioritário, a situação do contato e o canal brasileiro das 60 empresas. Cada ofício seleciona automaticamente o registro correspondente ao seu nome de arquivo e endereça o documento ao setor prioritário cadastrado; os demais campos, por serem informação de trabalho, aparecem apenas no diretório interno (`empresas/diretorio_contatos.tex`).

A base foi verificada em **13/09/2026** e deve ser conferida novamente imediatamente antes de cada envio.

## Fluxo operacional

1. Confirmar necessidade do laboratório.
2. Selecionar empresa e anexo técnico.
3. Gerar ofício individual.
4. Anexar dossiê institucional.
5. Conferir contato brasileiro.
6. Registrar no CRM.
7. Enviar o pacote.
8. Executar follow-up.
9. Em caso de interesse, realizar reunião técnica.
10. Formalizar a proposta pelos setores competentes do IFMA.
11. Receber, conferir e tombar os bens.
12. Medir impacto acadêmico.

## Observação administrativa

Os documentos são minutas de apoio. A prospecção não implica aceitação automática de doação, patrocínio ou obrigação. A formalização deve observar as normas vigentes do IFMA e da Administração Pública Federal.
