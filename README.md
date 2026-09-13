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

A pasta `empresas/` contém um modelo-base compartilhado e **60 ofícios LaTeX personalizados**, organizados por prioridade:

- **P1 — Máxima:** Schneider Electric, Vale, Eneva, Equatorial Energia, WEG, Rockwell Automation, Siemens, Altus, Intelbras, Petrobras, Schweitzer Engineering Laboratories (SEL), Endress+Hauser, Rohde & Schwarz, Infineon Technologies e Texas Instruments;
- **P2 — Alta:** Festo, SMC, ABB, Alcoa/Alumar, Suzano, Hitachi Energy, Eaton, Phoenix Contact, Emerson, Fluke, FNIRSI, RIGOL, SIGLENT, Universal Robots, FANUC, KUKA, OMRON, Beckhoff, WAGO, SICK, ifm electronic, Balluff, Pepperl+Fuchs, Weidmüller, Delta Electronics, Yokogawa, HIOKI, Megger, Minipa, Anritsu, VIAVI Solutions, STMicroelectronics e onsemi;
- **P3 — Oportunidade:** Keysight, Tektronix/Keithley, National Instruments, Yaskawa, Mitsubishi Electric, Bosch Rexroth, Cisco, Huawei, Dell Technologies, Lenovo, Instrutherm e Pico Technology.

A classificação indica prioridade de prospecção do DEE. Nem toda empresa possui programa público permanente de doação; quando não há confirmação, o modelo é tratado como prospecção estratégica de parceria, cessão, demonstração, apoio educacional ou eventual doação conforme política da empresa.

### Contatos no Brasil

O arquivo `empresas/contatos_brasil.tex` centraliza o **contato prioritário para doação/parceria** e o **canal brasileiro de cada uma das 60 empresas**. Cada ofício carrega automaticamente esse cadastro e exibe, junto ao destinatário, a situação do contato: operação oficial direta no Brasil, canal regional/distribuidor ou contato que deve ser confirmado antes do envio.

A base foi verificada em **13/09/2026**. Por serem informações externas sujeitas a alteração, telefone, e-mail, endereço e responsável nominal devem ser conferidos novamente no canal oficial imediatamente antes da expedição definitiva do ofício. A base evita duplicação: mudanças de contato devem ser feitas somente em `empresas/contatos_brasil.tex`.

### Cobertura tecnológica

A prospecção contempla Automação Industrial, Robótica, Redes Industriais, Instrumentação, Eletrônica Analógica e Digital, Telecomunicações/RF, Redes Ópticas, Sistemas Digitais, IoT, Eletrônica de Potência, Semicondutores de Potência, Medição Elétrica, Qualidade de Energia, Máquinas e Acionamentos, Instalações, Proteção, Subestações, Sistemas Elétricos de Potência, Smart Grid, Geração Distribuída, Aquisição de Dados, Manutenção, Pneumática, Hidráulica e Computação para Engenharia.

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

Os modelos institucionais utilizam `modelos/preambulo.tex`. Os documentos da pasta `empresas/` carregam `empresas/base_empresa.tex`, que centraliza o texto e a diagramação comum, e `empresas/contatos_brasil.tex`, que centraliza os destinatários e canais brasileiros.

Para gerar um ofício personalizado no Overleaf, selecione o arquivo `.tex` da empresa desejada como documento principal, use pdfLaTeX, preencha número/data do ofício e revise as quantidades. Os dados de contato do Chefe do DEE já estão incorporados ao modelo-base.

> **Observação:** os documentos são minutas de apoio administrativo. A formalização final deve observar as normas vigentes do IFMA e da Administração Pública Federal, bem como a análise dos setores competentes.
