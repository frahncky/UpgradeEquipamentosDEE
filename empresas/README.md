# Modelos de ofícios por empresa

Esta pasta contém **60 modelos LaTeX personalizados** para prospecção de doações e parcerias para o DEE/IFMA.

## Compilação no Overleaf

Cada arquivo numerado (`01_...tex` a `60_...tex`) é um documento LaTeX completo e pode ser selecionado diretamente como **Main document** no Overleaf.

Passos:
1. Abra **Menu** no Overleaf;
2. Em **Main document**, selecione o arquivo da empresa desejada;
3. Use compilador **pdfLaTeX**;
4. Clique em **Recompile**.

Os arquivos `base_empresa.tex` (corpo comum dos ofícios) e `contatos_brasil.tex` (base de contatos) não devem ser escolhidos como documento principal.

Fora do Overleaf, compile sempre a partir da raiz do repositório — `pdflatex empresas/01_schneider_electric.tex` — ou use `make oficios`.

## Contatos brasileiros centralizados

O arquivo `contatos_brasil.tex` contém o cadastro centralizado dos **60 contatos para prospecção**, um registro por empresa:

```latex
\ContatoEmpresa{chave}{empresa}{situação}{setor prioritário}{canal no Brasil}
```

A **chave** é o nome do arquivo do ofício sem a extensão (por exemplo, `01_schneider_electric`). O arquivo é carregado no preâmbulo de `base_empresa.tex`, que chama `\selecionaContatoPeloArquivo` e escolhe o registro correspondente ao documento em compilação. Não é necessário repetir telefone, e-mail, endereço ou setor em cada modelo individual.

O que aparece em cada documento:

- **no ofício enviado à empresa:** apenas o setor/contato prioritário, no campo *A/C*;
- **no diretório interno (`diretorio_contatos.tex`):** todos os registros, com situação do contato no Brasil, telefone, e-mail, endereço ou canal oficial quando confirmados, e a indicação expressa de distribuidor/canal regional quando não há filial brasileira direta.

A separação é proposital: o canal registrado traz observações de trabalho ("confirmar responsável nominal antes da expedição", "solicitar encaminhamento ao setor X") que não devem ser impressas no documento enviado à empresa. **O diretório é de uso interno e não entra no pacote de envio.**

Para cadastrar uma empresa nova, acrescente um `\ContatoEmpresa` com a chave igual ao nome do novo arquivo de ofício; se a chave não existir na base, o ofício recai no `\setorContato` declarado no próprio arquivo.

A última verificação da base foi realizada em **13/09/2026**. Antes da expedição definitiva, confirme o responsável nominal e os dados externos no site oficial da empresa, pois eles podem mudar.

## Rodada mais recente — Telecomunicações/RF e Eletrônica de Potência

- `54_rohde_schwarz.tex` — Rohde & Schwarz;
- `55_anritsu.tex` — Anritsu;
- `56_viavi.tex` — VIAVI Solutions;
- `57_infineon.tex` — Infineon Technologies;
- `58_stmicroelectronics.tex` — STMicroelectronics;
- `59_texas_instruments.tex` — Texas Instruments;
- `60_onsemi.tex` — onsemi.

Os modelos de Telecomunicações/RF contemplam análise de espectro, redes vetoriais, RF, comunicações móveis, fibras ópticas e teste de redes. Os modelos de Eletrônica de Potência contemplam MOSFET, IGBT, SiC, GaN, drivers, conversores, controle digital, acionamento de motores e plataformas de prototipagem.

Todos os modelos usam o padrão visual definido em `modelos/preambulo.tex` e os dados institucionais de contato do Chefe do DEE são inseridos pelo modelo-base.

## Diretório interno

`diretorio_contatos.tex` gera, em um único PDF, a lista completa dos 60 registros da base de contatos. Serve para conferência antes da expedição e para atualização periódica dos canais. Compile com `make diretorio` ou `pdflatex empresas/diretorio_contatos.tex` a partir da raiz.
