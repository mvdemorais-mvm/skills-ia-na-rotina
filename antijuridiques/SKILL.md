---
name: antijuridiques
description: Tira rebuscamento desnecessário e marca de IA de texto jurídico e institucional em português, sem baixar o registro formal. Substitui por linguagem direta os arcaísmos e fórmulas vazias como "mister se faz", "compulsando os autos", "outrossim" e "destarte"; desfaz nominalização empilhada, pleonasmo de ênfase e gerundismo de ofício. Use em peça, parecer, ofício, memorando, nota técnica e qualquer texto formal dirigido a órgão público.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
---

# Antijuridiquês

Enxuga sem baixar o registro. O texto continua formal — só para de ser ornamental.

**Isto não é tradução para leigo.** O registro permanece o mesmo. Escrever
"é necessário" no lugar de "mister se faz" não torna o texto informal: torna-o
formal e limpo, que é coisa diferente de formal e enfeitado.

---

## Arcaísmo e fórmula vazia

| Rebuscado | Direto |
|---|---|
| mister se faz | é necessário |
| compulsando os autos | ao examinar os autos |
| petitório vestibular / exordial | petição inicial |
| outrossim | além disso (ou corte) |
| destarte / dessarte | assim |
| por derradeiro | por fim |
| malgrado | apesar de |
| consoante o entendimento | segundo o entendimento |
| ab initio | desde o início |
| data maxima venia | com o devido respeito |
| perlustrando os fólios | ao ler os autos |
| a peça incoativa | a inicial |
| esposar o entendimento | adotar o entendimento |
| carreado aos autos | juntado aos autos |
| in casu | no caso |

**Fórmula de tratamento repetida:** preserve a **primeira** ocorrência de cada
fórmula por seção e corte as repetições seguintes. "Egrégio Tribunal" no início
da razão recursal fica; "egrégio" outra vez três parágrafos depois, sai. O
endereçamento nunca é tocado (ver zonas protegidas).

## Nominalização empilhada

Substantivo abstrato encadeado com "de" esconde o verbo e alonga a frase.

> "a realização da análise da procedência do pedido"
> → "analisar se o pedido procede"

> "para fins de obtenção da declaração de extinção"
> → "para obter a extinção"

> "procedeu-se à efetivação da intimação"
> → "procedeu-se à intimação"

Note que a reescrita **não** inventou quem foi intimado. O original não diz, e
acrescentar participante viola a regra de integridade.

## Pleonasmo de ênfase

O jurídico dobra adjetivos para dar força. Escolha um.

> "prova cabal e inequívoca" → "prova inequívoca"
> "clara e evidente violação" → "violação evidente"
> "total e completo descumprimento" → "descumprimento total"
> "elencar um rol" → "listar" / "arrolar"

## Ordem inversa gratuita e voz passiva sem motivo

> "Da análise dos autos, verifica-se que assiste razão à parte."
> → "A análise dos autos mostra que assiste razão à parte."

Desfaz a inversão sem trocar o registro e sem mexer em "assiste razão a", que é
construção consagrada.

Passiva só quando o agente é irrelevante ou desconhecido. "Foi determinado pelo
juízo" → "o juízo determinou".

## "Sendo que" e gerundismo de ofício

Vício estrutural de redação oficial, diferente do gerúndio de análise rasa.

> "Sendo que o prazo venceu" → "Como o prazo venceu" / "O prazo venceu, e"
> "Estaremos analisando o pedido" → "Analisaremos o pedido"
> "Vimos por meio desta informar" → "Informamos"
> "Venho por meio deste solicitar" → "Solicito"

---

## Limpeza de marca de IA

Em registro formal, uma limpeza geral de marca de IA não serve, porque várias
regras dela atropelam texto jurídico. Este é o subconjunto **seguro**, aplicado aqui:

- **Vocabulário de IA:** "cabe ressaltar", "é importante salientar", "vale
  destacar", "cenário em constante evolução", "nesse sentido", "sob essa ótica",
  "no que tange a", "à luz de" (quando puramente decorativo)
- **Title Case em títulos** — em português só a primeira palavra e nomes próprios
  levam maiúscula. **Exceto** ementa, cabeçalho de acórdão, súmula e qualquer
  trecho em caixa alta dentro da zona intocável: ali a caixa é do original.
- **Emoji decorativo**
- **Travessão epidêmico.** A marca de IA mais visível em português. **O teste é
  de função, não de contagem.** Legítimo é aparte: vem em PAR, interrompe o
  período e caberia entre parênteses. Epidêmico é solteiro, antes da última
  oração, fazendo pausa dramática no lugar de um sinal que diz mais:

  | O que a segunda parte faz | Sinal certo |
  |---|---|
  | explica, detalha ou exemplifica a primeira | **dois-pontos** |
  | coordena, continua na mesma altura | **vírgula** |
  | já era outra frase fingindo não ser | **ponto** |
  | interrompe de verdade (aparte) | travessão **em par**, ou parênteses |

  Se trocar por `:`, `,` ou `.` não perde nada, era pausa: corte. **Corte o
  solteiro que faz pausa, preserve o par que faz aparte** — "não corte travessão
  legítimo" não quer dizer "não mexa em travessão". Separador de nome e subtítulo
  em título fica. Zero travessão em prosa é resultado normal, não texto travado
 .
- **Gerúndio de análise rasa no fim da frase:** "demonstrando", "evidenciando",
  "ressaltando a importância", "garantindo"
- **Negrito mecânico em termo solto dentro de frase corrida.** Não mexa na
  estrutura de tópicos de documento oficial — subtítulo em negrito seguido de
  dois-pontos é o formato padrão de nota técnica e parecer, e é para ficar.

**Fica de fora todo conselho de persona de limpezas gerais de IA.** Não use primeira pessoa,
não "permita alguma desordem", não injete opinião nem sentimento, e **nunca**
reduza uma lista de três itens para dois. Numa peça, uma lista de três é um rol
de fundamentos, e apagar um item apaga um argumento.

Esta skill mexe, sim, na **voz do período** — passiva sem motivo, ordem inversa,
nominalização. Isso é diferente de persona, e é trabalho dela.

---

## Zonas protegidas

Além da zona intocável geral (citação literal, ementa, transcrição, nome próprio,
nome de órgão, número de processo, valores, marcação; dona: a skill `texto-pronto`), esta
skill tem duas próprias.

### 1. Fórmula de tratamento e endereçamento obrigatória

Exigência do rito, não enfeite. Não toque:

- "Excelentíssimo Senhor Doutor Juiz de Direito da Vara…"
- "Egrégio Tribunal", "colenda Turma", "eminente Relator"
- Fecho e vocativo do padrão ofício

### 2. Termo técnico

Termo de arte é precisão, não rebuscamento. Trocar por sinônimo "mais simples"
destrói o texto.

Não toque: "prescrição intercorrente", "exceção de pré-executividade", "certidão
de dívida ativa", "embargos de declaração", "coisa julgada", "litispendência",
"fato gerador", "lançamento tributário", "sujeito passivo".

Na dúvida entre arcaísmo e termo técnico, **presuma termo técnico e não mexa**.

---

## Saída

O texto enxuto e nada mais. A contagem de correções e o formato final são
responsabilidade da `revisor-pt-br`, que roda depois desta.

Se o texto não tiver juridiquês, devolva-o intacto e diga isso em uma linha.

Nunca acrescente fato, participante ou valor ausente do original, nem remova
fundamento. Verificação mecânica opcional (candidatos, não veredito):
`python3 ../texto-pronto/lint.py <arquivo>`.
