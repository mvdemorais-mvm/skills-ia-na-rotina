---
name: conferencia-antes-de-assinar
description: Monta a lista de conferência de um texto feito com ajuda de IA antes de assinar ou protocolar. Separa o que foi conferido do que não foi, e diz onde conferir cada item (números e datas, citações de lei, súmula e jurisprudência, nomes e valores, fatos sem documento, dado pessoal desnecessário). Use sempre que o usuário disser que vai assinar, protocolar, enviar ou publicar texto jurídico ou institucional produzido ou revisado com IA.
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Conferência antes de assinar

A IA escreve com segurança mesmo quando erra. Esta skill não revisa estilo nem
gramática: ela lista o que um humano precisa verificar na fonte antes de assinar.

## Regras de conduta

- **Nunca aprove.** Quem assina é o autor. Esta skill entrega uma lista, não um
  "pode protocolar".
- **Nunca invente** artigo, súmula, precedente, ementa, número ou data para
  "completar" a conferência. Se não achou na fonte fornecida, diga "não conferido".
- Só marque "conferido" o que foi comparado com documento que o usuário forneceu
  nesta conversa (autos, norma, acórdão colado ou anexado). Conhecimento do
  próprio modelo não conta como conferência.

## O que conferir

**(a) Números e datas.** Cada número, percentual, prazo e data contra a fonte
(documento dos autos, planilha, norma). Conferir também a conta: soma, diferença
entre datas, contagem de prazo.

**(b) Citação jurídica.** Para cada lei, artigo, súmula, tese ou julgado:
1. Existe? 2. O texto citado bate, palavra por palavra, com a fonte oficial
(site do Planalto para lei federal; site do tribunal para súmula e acórdão)?
3. Ainda está em vigor, sem alteração ou superação?
Marque a origem de cada citação: "do documento que você enviou", "de busca web
(não é base jurídica especializada)" ou "do treinamento do modelo, pode estar
desatualizado, verifique". Citação sem origem comprovável fica "não conferida".

**(c) Identificação.** Nome de parte, número de processo, número de documento e
valores contra os autos, caractere por caractere.

**(d) Fato sem documento.** Toda afirmação de fato que não tenha documento
sustentando (folha, anexo, certidão). Liste e pergunte ao autor qual documento
a prova; se não houver, o autor decide se retira ou assume.

**(e) Dado pessoal desnecessário.** CPF, endereço, saúde, dado de terceiro ou de
menor que não precisa estar no texto. Sugira retirar ou abreviar (LGPD).

## Saída

Tabela com cinco colunas: item, trecho, situação (conferido / não conferido /
divergente), fonte usada e onde conferir. Depois, uma linha: "Itens não
conferidos: N. A decisão de assinar é sua."

Se o texto não trouxer o documento de apoio, a situação é "não conferido" e a
coluna "onde conferir" aponta a fonte oficial (Planalto, site do tribunal, os
próprios autos).
