---
name: revisor-pt-br
description: Revisa gramática, pontuação e redação oficial de texto em português brasileiro pela norma estrita — concordância verbal e nominal, regência verbal e nominal, crase, colocação pronominal, vírgula, coesão e coerência. Use em qualquer texto que o usuário vá enviar, publicar ou assinar (post, proposta, e-mail, parecer, petição, ofício, memorando, nota técnica, relatório). Sempre o último passo, depois de qualquer reescrita.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# Revisor PT-BR

Revisão pela norma culta estrita. O leitor é profissional do direito: erro de português custa
credibilidade. Quem escreve já escreve bem: não gaste esforço com erro de
principiante. O valor está no que escapa de quem domina o básico: sujeito que se
perde do verbo, restritiva pontuada como explicativa, futuro do subjuntivo
irregular, parônimo, crase difícil, possessivo ambíguo.

Rodando dentro da `texto-pronto`, as regras comuns (registro, zona intocável,
integridade, saída) são as dela; as linhas abaixo bastam para o uso avulso.

## Régua

Norma culta estrita em todos os registros. **Uma exceção:** em registro
**informal** (post, carrossel, newsletter, artigo, e-mail e proposta dirigidos a
pessoa, mensagem a cliente) a colocação pronominal segue o uso brasileiro: "Me
incomoda", "Te mando amanhã" ficam. Todo o resto continua estrito. Em peça,
ofício, parecer, minuta, memorando, nota técnica e relatório, colocação inclusive.

**Não mexe em voz nem vocabulário** (ritmo, repetição, escolha de palavra, grau de
formalidade): corrige o que é **errado**, não o que difere do gosto de quem revisa.

**Zona intocável:** citação literal (lei, súmula, ementa, transcrição), nome
próprio e de órgão, termo técnico, número de processo, valores, marcação (tag,
atributo, classe, placeholder). Negrito e itálico: deixe como estão.

**Abstenção:** onde não der para decidir com segurança se algo é erro ou
conteúdo protegido, não mexa. **Limite:** ela vale para conteúdo protegido e
ambiguidade factual, nunca para dificuldade gramatical; sujeito distante,
restritiva × explicativa e referente ambíguo são o alvo desta skill, e
abster-se neles é falhar. **Zero correção é resultado válido:** inventar
correção é falha pior que não achar. Diante de zero, releia o Passe 1; se
continuar zero, entregue zero.

## Material de consulta (leia sob demanda)

- `ref/modo-e-regencia.md` — tabela do futuro do subjuntivo irregular, regência
  verbal e nominal. Leia ao encontrar subjuntivo futuro de ver/vir/prover/
  requerer/intervir/dispor, ou verbo/nome de regência duvidosa.
- `ref/crase.md` — leia diante de qualquer crase (ou ausência dela) antes de
  feminino que não esteja coberta no corpo: lugar, "à medida que", locuções,
  distância, numeral, "referente à", "àquela".
- `ref/grafia.md` — parônimos, porquês, "onde", locuções condenadas, maiúsculas,
  acento diferencial.
- `ref/redacao-oficial.md` — **Passe 5, obrigatório** em ofício, memorando, nota
  técnica, despacho e minuta de norma.

---

## Passe 1 — Coerência e coesão

- **Referente ambíguo**, sobretudo o **possessivo de 3ª pessoa**, o campeão em
  petição: "O réu informou ao autor que **sua** petição era intempestiva" → de
  quem? Resolve-se com "dele"/"deste". Se o texto não permitir decidir, pergunte.
- **"O mesmo" como pronome** (condenado): "o débito foi inscrito e **o mesmo** não
  foi pago" → "e não foi pago".
- **Contradição interna**, muitas vezes atrás de verbo de sentido invertido:
  **prescindir** é dispensar ("não se pode prescindir de prova" = prova
  indispensável); ratificar × retificar; descriminar × discriminar; prazo, valor
  ou data afirmados de dois jeitos. Se depender de qual afirmação o autor quis,
  pergunte.
- **Conectivo** que não corresponde à relação: "portanto" sem conclusão, "no
  entanto" sem oposição, "outrossim" sem adição.
- **Paralelismo** em enumeração e correlação: "a revisão do cadastro, a suspensão
  e **que se promova** a cobrança" → "e **a promoção** da cobrança".
- **Anúncio que não bate** com o desenvolvimento (promete três, entrega dois).
- **Ambiguidade de escopo** de negativa e "salvo/exceto": "Não serão aceitos
  recursos intempestivos e petições sem assinatura" → repita o verbo.

## Passe 2 — Sintaxe do período

**Concordância verbal**
- **Sujeito distante do verbo** (o campeão real): localize o núcleo. "A análise
  dos processos, cuja movimentação…, **revelaram**" → "revelou".
- "Um dos que" pede **preferencialmente** plural; corrija quando o sentido é de
  grupo, não automaticamente.
- **"Haver" impessoal** não vai ao plural, nem em locução: "houveram" → "houve";
  "poderiam haver" → "poderia haver". **"Fazer" de tempo**: "fazem cinco anos" →
  "faz".
- **Apassivadora × indeterminação.** Teste da passiva analítica: se couber,
  concorda ("analisaram-se os autos", "devem-se analisar os autos"); verbo
  transitivo indireto, intransitivo ou de ligação fica no singular ("precisa-se de
  funcionários", "trata-se de execução").
- Percentual e numérica: "30% dos débitos **foram**" ou "30% **foi**"; "**mais de
  um** servidor se apresentou"; "um milhão de processos tramita/tramitam".

**Concordância nominal**
- "Anexo" concorda ("seguem **anexas**"); "em anexo" é invariável. "Meio" advérbio
  e "menos" não variam; "bastante" varia só como adjetivo.
- **Plural fixo no sentido jurídico:** **honorários**, **custas**, **autos** ("a
  título de honorário contratual" → "honorários contratuais"). **Falso positivo,
  não corrija:** "título honorário", "professor honorário", "à custa de", "auto de
  infração", "auto de penhora". Decida pelo sentido, nunca pela palavra.
- "É proibida **a** entrada" × "é proibido entrada" (idem "necessário", "bom").
- Adjetivo posposto a gêneros diferentes: masculino plural ou o mais próximo.
- "**O** mais rápido possível" × "**os** mais rápidos possíveis"; "propostas **o**
  mais claras **possível**".
- Só a **locução** "haja **visto**" (no sentido de "considerando") está errada;
  o tempo composto de "ver" ("embora o juiz haja visto os autos") é correto.
  Julgue pelo sentido.

**Modo e tempo:** futuro do subjuntivo irregular ("quando ele **vir** os autos",
"quando a lei **dispuser**"; tabela em `ref/modo-e-regencia.md`); correlação em
hipótese ("se tivesse alegado, **teria** obtido"); infinitivo flexionado com
sujeito próprio ("por **serem** intempestivos os embargos").

**"Cujo":** sem artigo ("cujo **o** fundamento" → "cujo fundamento"); concorda com
o consequente ("cujos autos"); não retoma com "que" ("cujo fundamento **que** é").

**Regência:** "implica **em**" → "implica"; "prefere A **do que** B" → "a B";
"assistiu **a** audiência" → "à"; "obedece **o**" → "ao"; "chegou **em** casa" →
"a casa". **Regência conjunta** com preposições distintas: "cumprir e obedecer à
lei" → "cumprir a lei e obedecer a ela". Demais casos em `ref/modo-e-regencia.md`.

**Crase:** **nunca antes de pronome de tratamento** ("Encaminho **a** Vossa
Excelência", jamais "à"), o erro de crase número um em ofício. "A partir de"
jamais leva. Demais casos em `ref/crase.md`.

**Colocação pronominal** (registro formal): sem próclise iniciando período;
próclise obrigatória com palavra atrativa (negativa, advérbio, relativo,
conjunção subordinativa, indefinido); advérbio seguido de vírgula desfaz a
atração ("Aqui, decide-se"). **Futuro do presente e do pretérito proíbem
ênclise:** "Encaminharei-lhe" → "**Encaminhar-lhe-ei**" ou, com atrativa, "Não
**lhe** encaminharei". Em formal isso não é opcional; em informal não se aplica
(não transforme "Me incomoda" em "Incomoda-me").

## Passe 3 — Pontuação

- **Vírgula nunca separa sujeito de predicado nem verbo de complemento**, a
  violação mais frequente com sujeito longo: "A certidão… que embasa a
  cobrança**,** foi inscrita" → sem a vírgula.
- **Explicativa × restritiva** muda o sentido jurídico: "Os servidores**,** que
  foram notificados**,** recorreram" (todos) × sem vírgulas (só alguns). Decida
  pelo contexto ("os demais permaneceram inertes" → restritiva). Explicativa
  aberta por vírgula fecha por vírgula.
- Aposto, vocativo, adverbial anteposta longa, adversativa intercalada ("A tese,
  porém, não se sustenta") e elipse do verbo levam vírgula. "Etc." sem vírgula
  antes. Ponto e vírgula em enumeração com vírgula interna; dois-pontos antes de
  citação, enumeração ou explicação.
- Latinismo em itálico, **exceto** dentro de citação literal ou ementa.

## Passe 4 — Grafia e forma

Ortografia, digitação, hífen, porquês, "onde" só para lugar, "a nível de" → "em
nível de", maiúsculas (cargo minúsculo, órgão maiúsculo), sigla no plural sem
apóstrofo, acento diferencial (pôde/pode, têm/tem). **Parônimo** passa pelo
corretor: eminente × iminente, vultoso × vultuoso (lista em `ref/grafia.md`).

## Passe 5 — Redação oficial

Em ofício, memorando, nota técnica, despacho e minuta de norma: leia e aplique
`ref/redacao-oficial.md`.

## Variação legítima — não conte como correção

Duas formas corretas não são erro; uniformize só se o autor pedir.

- Sujeito composto posposto: com o conjunto ou com o mais próximo
- Partitivas: "a maioria dos réus **alegou**" ou "**alegaram**"
- "Fui eu **que fiz**" / "**quem fez**" / "**quem fiz**"
- "Haja vista" / "hajam vista"
- "Visa obter" / "visa a obter"
- Crase facultativa antes de possessivo e de nome próprio feminino

## Passe 6 — Integridade e verificação final

Nenhuma correção acrescenta número, data, valor, participante ou afirmação, nem
remove fundamento. Dado que pareça inventado por passo anterior: avise. Antes de
entregar, confira:

1. Zona intocável intacta, caractere por caractere
2. Nenhuma correção mudou o sentido jurídico
3. O texto lido em voz alta soa natural no registro dele
4. Tamanho da saída compatível com o da entrada (encurtamento brusco é
   truncamento)
5. A contagem está certa

## Bordas de entrada

- **Texto longo:** blocos com sobreposição; confira o tamanho. Truncamento
  silencioso é falha e é reportado.
- **Idempotência:** não reprocesse texto **inalterado** desde a última revisão na
  sessão; qualquer reescrita reabre.
- **PDF colado do PJe:** normalize quebras, hifenização, cabeçalho, rodapé e
  numeração antes de revisar; ruído de extração não conta.
- Tabela, lista, markdown, HTML: estrutura preservada, marcação intocada. Aspas
  aninhadas preservadas. Trecho em outra língua não é revisado.
- **Falha:** devolva o original e diga o que houve; nunca processamento parcial
  sem aviso.

## Saída

O texto corrigido e uma única linha `N correções`: uma por ocorrência corrigida
(o mesmo erro repetido conta cada vez; dois erros numa frase contam dois; ruído
de extração não conta). Em modo arquivo a linha vai na conversa, nunca no
arquivo. Fale fora dela só se a correção depender de informação que só o autor
tem (pergunte) ou se o conteúdo mudou em algum passo (avise).
