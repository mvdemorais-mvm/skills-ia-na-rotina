---
name: texto-pronto
description: Prepara texto em português brasileiro para ser enviado, publicado ou assinado. Limpa marca de IA, tira juridiquês e revisa a gramática por último, na ordem que o registro pede. Use SEMPRE que produzir post, carrossel, newsletter, artigo, proposta, e-mail de prospecção, parecer, minuta, petição, nota técnica, ofício, memorando, relatório ou mensagem a cliente, e de novo quando esse texto for alterado. Não use em resposta de conversa, código, mensagem de commit, diagnóstico interno nem documentação de repositório.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Skill
  - Bash
  - AskUserQuestion
---

# Texto pronto

Orquestra a preparação de texto entregável. O registro escolhe os passos, não
você. Esta skill é **dona das regras comuns** da cadeia (registro, zona
intocável, integridade, saída, quando falar); `antijuridiques` e `revisor-pt-br`
guardam só uma linha de cada uma para quando rodam sozinhas.

## O fluxo

```
1. registro (em silêncio)
1b. peça (petição, recurso, contestação, parecer, manifestação; não ofício,
    memorando nem nota técnica): skill pecas-para-ia sobre o texto; a versão
    adaptada dela é a entrada do passo 2
2. voz:  INFORMAL → ler ref/informal.md e aplicar
         FORMAL   → skill antijuridiques
3. lint: python3 lint.py <arquivo>  (na pasta desta skill; ou via stdin)
         → julgar cada achado; o que procede, corrigir antes do passo 4
4. skill revisor-pt-br — sempre a última, porque reescrita introduz erro
5. entrega: texto + linha "N correções"
```

**Lint (passo 3).** Roda sobre o texto já reescrito, antes da revisora. Cada
linha `linha:trecho:regra` é candidato, não veredito: descarte o que cair em zona
intocável, em citação ou em uso legítimo ("é o mesmo", travessão em par). Achado
de voz (arcaísmo, vocabulário de IA, travessão solteiro, Title Case, emoji) você
corrige; achado de norma (haver, crase, "implica em", ênclise no futuro) vai
junto para a revisora conferir. Lint vazio não dispensa o julgamento dos passos
2 e 4. Se ele imprimir `ERRO`, siga sem ele.

Em peça (petição, recurso, parecer), a estrutura de leitura por IA (síntese no
topo, título que afirma a tese, um argumento por tópico e pedidos numerados) é
protegida: a limpeza não funde a síntese ao corpo nem troca o título-tese por
título genérico. Antes de entregar, a peça não pode conter `[folha?]` nem
`[conferir]`: se houver, avisar o autor e listar onde.

**Peça (passo 1b).** Quem cria a estrutura de leitura por IA é a `pecas-para-ia`
(síntese no topo, títulos-tese, pedidos numerados). Roda antes da voz, para a
limpeza trabalhar sobre a peça já estruturada. Só registro formal do tipo peça;
ofício, memorando e nota técnica ficam fora. Se o texto é **modelo de gerador**
(petições em lote), aplique ao modelo, uma vez, nunca peça a peça: a estrutura
nasce no molde.

**Por que o caminho formal não usa a limpeza informal:** ela troca aspas de
citação, ataca caixa alta de ementa, rotaciona termo técnico e mexe em
quantidade de itens; numa petição com três fundamentos, isso apaga um. O
subconjunto seguro para formal está dentro da `antijuridiques`.

## Registro (lista canônica — a única)

| Registro | Textos |
|---|---|
| **Informal** | post, carrossel, newsletter, artigo, e-mail e proposta dirigidos a pessoa, mensagem a cliente |
| **Formal** | peça, petição, minuta, parecer, ofício, memorando, nota técnica, despacho, relatório, e qualquer texto dirigido a órgão público — inclusive proposta comercial endereçada a órgão |

Na dúvida, formal. Identifique sem anunciar. O registro decide o caminho e a
exceção de colocação pronominal (só informal). A régua gramatical é estrita nos
dois, então errar o registro nunca degrada a gramática, só a voz.

**Texto misto** (proposta com ementa transcrita, post que cita petição) é tratado
por bloco: o transcrito entra na zona intocável; o resto segue o registro
dominante.

## Quando disparar

**Dispara:** o que o autor vai **enviar, publicar ou assinar** (lista da
descrição). Nota técnica que nasceu interna e vai à Secretaria dispara.
**Não dispara:** conversa, código e comentário de código, commit, análise
interna, documentação de repositório, handoff, `SKILL.md`.

**Reabertura obrigatória.** Texto que já passou pela cadeia e foi **alterado**
(cortar, reescrever, acrescentar, reordenar — inclusive pelo próprio assistente a
pedido do autor) volta para a **cadeia inteira**, não só para a revisora. Numa
alteração quebram duas coisas que não são gramática: o que sobrou passa a mentir
(título que contava três itens, comparativo sem termos, fecho que promete bloco
apagado, remissão a trecho que sumiu) e o que entrou nunca passou por passo
nenhum.

## Zona intocável (vale para todos os passos)

Nunca altere: citação literal de lei, súmula, ementa e transcrição; nome próprio
e nome de órgão; termo técnico; número de processo; valores; marcação (tag,
atributo, classe, placeholder de template). Ênfase (negrito, itálico) não é
marcação, mas também não é assunto da revisão gramatical.

## Integridade

Nenhum passo acrescenta número, data, valor, participante ou afirmação ausente do
original, nem remove fundamento, nem muda a quantidade de itens de uma lista. Se o
conteúdo mudou, avise em vez de entregar calado.

## Fronteira entre os passos

- `ref/informal.md` manda em **ritmo e marca de IA** do texto informal (sem
  inventar persona)
- `antijuridiques` manda em **vocabulário, voz do período e marca de IA** do
  texto formal, travessão epidêmico incluído
- `revisor-pt-br` manda em **correção**; só desfaz escolha dos passos anteriores
  quando ela gerou erro gramatical
- `pecas-para-ia` manda na **estrutura de leitura por IA** da peça (passo 1b);
  os passos seguintes não a desfazem: síntese no topo, título-tese, um argumento
  por tópico, pedidos numerados; a peça não sai com `[folha?]` nem `[conferir]`

**Regra sem dono não é regra.** Ao herdar qualquer regra da limpeza informal para
o caminho formal, confirme que um passo formal a executa.

## Entrada e saída

Caminho de arquivo ou texto direto. Disparo automático sobre texto recém-produzido
na sessão opera sobre ele antes de entregá-lo.

- **Modo arquivo só para `.md` e `.txt`.** `.docx`, `.pptx`, `.pdf` e HTML: extraia,
  processe e devolva o texto; nunca reescreva no lugar. Em nenhum formato toque em
  tag, atributo, classe ou placeholder.
- **Gravação só com rede:** arquivo em git grava direto; fora de git, crie `.bak`
  com o original **antes**. Nunca sobrescreva sem uma das duas.
- **Antes de gravar texto com nome de parte, CPF, CNPJ ou número de processo,
  confira se esses dados precisam mesmo estar ali (LGPD) e se o arquivo ficará em
  local adequado.**
- **Saída:** o texto corrigido e, depois, uma única linha `N correções` (uma por
  ocorrência corrigida pela revisora; ruído de extração não conta). Não é lista de
  mudanças: é o sinal que separa "rodou" de no-op. Em modo arquivo a linha vai
  **na conversa, nunca dentro do arquivo**.

## Quando falar

Fora da linha de contagem, só em dois casos:

1. A correção depende de informação que só o autor tem (referente ambíguo ou
   contradição cuja escolha trocaria o sentido jurídico): pergunte.
2. O conteúdo mudou (dado acrescentado ou trecho perdido): avise.

## Prova de pronto

Lint: `python -m pytest tests/` nesta pasta.
