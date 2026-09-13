# Pacote padrão de envio

Cada empresa deve receber um pacote enxuto, com os arquivos em PDF e nomes padronizados.

## Arquivos
1. `01_Oficio_DEE_IFMA_<EMPRESA>.pdf`
2. `02_Resumo_Executivo_DEE_IFMA.pdf`
3. `03_Anexo_Tecnico_<EMPRESA>.pdf`
4. `04_Dossie_Institucional_DEE_IFMA.pdf`, quando adequado ao estágio da conversa
5. quando necessário, `05_Plano_Equipamentos_<EMPRESA>.pdf`

A ordem segue a composição definida em `pacotes_prioritarios.md`. O **resumo executivo**
(`dossie/03_resumo_executivo.tex`) vem logo depois do ofício porque tem uma página só, e é
por ela que quem abre o pacote pela primeira vez decide o encaminhamento; o dossiê completo
fica para quem quiser aprofundar.

## Corpo do envio
A mensagem deve:
- identificar o IFMA e o DEE;
- explicar em 2-3 linhas o objetivo;
- mencionar por que aquela empresa foi escolhida;
- indicar que a lista é adaptável ao portfólio/disponibilidade;
- solicitar encaminhamento ao setor correto se o destinatário não for responsável;
- oferecer reunião técnica e visita aos laboratórios.

## Nome do assunto
`Parceria educacional e modernização de laboratórios - DEE/IFMA - <EMPRESA>`

## Antes de enviar
- conferir número/data do ofício;
- gerar o resumo executivo atualizado (`make dossie`);
- confirmar contato em `empresas/contatos_brasil.tex` (ou no PDF de `empresas/diretorio_contatos.tex`);
- verificar se o nome da empresa está correto;
- revisar quantidades do anexo;
- gerar PDFs finais;
- registrar data no CRM;
- programar follow-up.
