# Upgrade de Equipamentos do DEE/IFMA

Repositório de modelos institucionais em LaTeX para organizar a prospecção, formalização e acompanhamento de doações e parcerias destinadas à modernização dos laboratórios do Departamento de Eletroeletrônica (DEE) do IFMA – Campus São Luís/Monte Castelo.

## Estrutura

### Modelos institucionais

- `modelos/preambulo.tex` — padrão visual comum aos documentos;
- `modelos/01_projeto_mae.tex` — Programa de Modernização Tecnológica dos Laboratórios do DEE;
- `modelos/02_solicitacao_suap.tex` — solicitação interna para abertura/tramitação no SUAP;
- `modelos/03_oficio_empresa.tex` — ofício institucional genérico de prospecção;
- `modelos/04_manifestacao_interesse.tex` — minuta de manifestação de interesse da empresa;
- `modelos/05_plano_equipamentos.tex` — relação técnica de equipamentos e justificativas;
- `modelos/06_relatorio_recebimento.tex` — relatório de recebimento, conferência e encaminhamento ao patrimônio;
- `modelos/07_checklist_procedimento.tex` — checklist do fluxo administrativo completo.

### Modelos personalizados por empresa

A pasta `empresas/` contém um modelo-base compartilhado e **30 ofícios LaTeX personalizados**, organizados por prioridade:

- **P1 — Máxima:** Schneider Electric, Vale, Eneva, Equatorial Energia, WEG, Rockwell Automation, Siemens, Altus, Intelbras e Petrobras;
- **P2 — Alta:** Festo, SMC, ABB, Alcoa/Alumar, Suzano, Hitachi Energy, Eaton, Phoenix Contact, Emerson e Fluke;
- **P3 — Oportunidade:** Keysight, Tektronix/Keithley, National Instruments, Yaskawa, Mitsubishi Electric, Bosch Rexroth, Cisco, Huawei, Dell Technologies e Lenovo.

Cada arquivo de empresa já contém área de atuação, setor recomendado para prospecção, estratégia, proposta de cooperação, equipamentos/quantidades sugeridos e canal institucional oficial.

## Fluxo recomendado

1. Levantamento das necessidades do DEE;
2. Elaboração do Projeto de Modernização;
3. Abertura de processo administrativo no SUAP;
4. Ciência/autorização da Direção-Geral e setores competentes;
5. Prospecção e envio de ofícios individualizados às empresas;
6. Formalização da intenção de doação/parceria;
7. Análise administrativa, jurídica e patrimonial;
8. Celebração do instrumento aplicável;
9. Recebimento e conferência dos bens;
10. Tombamento/registro patrimonial e destinação aos laboratórios.

## Uso

Os modelos institucionais utilizam `modelos/preambulo.tex`. Os documentos da pasta `empresas/` carregam `empresas/base_empresa.tex`, que centraliza o texto e a diagramação comum.

Para gerar um ofício personalizado no Overleaf, selecione o arquivo `.tex` da empresa desejada como documento principal. Antes da emissão, preencha os campos de número/data do ofício, e-mail e telefone institucional e revise as quantidades solicitadas.

> **Observação:** os documentos são minutas de apoio administrativo. A formalização final deve observar as normas vigentes do IFMA e da Administração Pública Federal, bem como a análise dos setores competentes.
