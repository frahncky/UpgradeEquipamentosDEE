# Sistema de prospecção

Esta pasta transforma os 60 ofícios em um processo gerenciável.

## Arquivos
- `ranking_60_empresas.csv`: score interno e ondas de contato;
- `top_10_primeiro_contato.md`: empresas que devem iniciar a campanha;
- `crm_prospeccao.csv`: controle de contatos e próximos passos;
- `calendario_followup.md`: cadência de acompanhamento;
- `pacote_envio.md`: documentos e checklist de expedição;
- `modelos_email.md`: mensagens para primeiro contato e follow-up;
- `fontes_priorizacao.md`: evidências públicas usadas na Onda 1.

A coluna **`Chave`** do ranking e do CRM é o identificador da empresa — o mesmo nome de arquivo usado em `empresas/` e em `empresas/contatos_brasil.tex`. É por ela que `make verificar` liga as três fontes e acusa divergência de prioridade, empresa faltando ou planilha fora de sincronia; os nomes escritos por extenso variam entre os arquivos e não servem para isso.

Os contatos das empresas não ficam aqui: a base é `empresas/contatos_brasil.tex`, e o PDF de conferência é `empresas/diretorio_contatos.tex`.

## Score
O score é uma ferramenta de gestão e não uma previsão de sucesso. Ele considera:
- aderência tecnológica: 30 pontos;
- evidência de apoio educacional/doação: 25;
- presença/operação no Brasil: 15;
- proximidade Maranhão/Nordeste: 15;
- impacto potencial: 10;
- clareza/facilidade do canal de contato: 5.
