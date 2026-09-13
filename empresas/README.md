# Modelos de ofícios por empresa

Esta pasta contém **60 modelos LaTeX personalizados** para prospecção de doações e parcerias para o DEE/IFMA.

## Compilação no Overleaf

Cada arquivo numerado (`01_...tex` a `60_...tex`) é um documento LaTeX completo e pode ser selecionado diretamente como **Main document** no Overleaf.

Passos:
1. Abra **Menu** no Overleaf;
2. Em **Main document**, selecione o arquivo da empresa desejada;
3. Use compilador **pdfLaTeX**;
4. Clique em **Recompile**.

O arquivo `base_empresa.tex` contém o corpo comum dos ofícios e não deve ser escolhido como documento principal.

## Contatos brasileiros centralizados

O arquivo `contatos_brasil.tex` contém o cadastro centralizado dos **60 contatos para prospecção**. O arquivo é carregado automaticamente por `base_empresa.tex`; portanto, não é necessário repetir telefone, e-mail, endereço ou setor em cada modelo individual.

Cada ofício passa a mostrar:
- o setor/contato prioritário para doação, parceria ou apoio educacional;
- a situação do contato no Brasil;
- telefone, e-mail, endereço ou canal oficial quando confirmados;
- indicação expressa de uso de distribuidor/canal regional quando não foi confirmada uma filial brasileira direta.

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
