# Kit de skills para texto jurídico com IA

Cinco skills em português brasileiro. Cada uma é uma pasta com um `SKILL.md`.

- `texto-pronto`: orquestra a preparação do texto (registro, limpeza, lint e revisão final).
- `antijuridiques`: tira rebuscamento e marca de IA de texto formal, sem baixar o registro.
- `revisor-pt-br`: revisa gramática, pontuação e redação oficial pela norma estrita (consulta em `ref/`).
- `pecas-para-ia`: reorganiza petição, recurso ou parecer para ser bem lido por IA, sem acrescentar fato.
- `conferencia-antes-de-assinar`: lista o que conferir na fonte antes de assinar ou protocolar.

O `texto-pronto` chama `antijuridiques`, `revisor-pt-br` e `pecas-para-ia`; instale as quatro juntas.

## Claude Code

Baixe o repositório https://github.com/mvdemorais-mvm/skills-ia-na-rotina (botão "Code" › "Download ZIP", ou `git clone`) e copie cada pasta para `~/.claude/skills/`:

    cp -r texto-pronto antijuridiques revisor-pt-br pecas-para-ia conferencia-antes-de-assinar ~/.claude/skills/

Abra uma nova sessão. As skills disparam pela descrição ou pelo nome (por exemplo, "use a texto-pronto neste e-mail").
O `lint.py` do `texto-pronto` exige apenas Python 3; testes: `python -m pytest texto-pronto/tests/`.

## ChatGPT, Gemini ou outro assistente

Crie um projeto, GPT ou Gem e cole o conteúdo de um `SKILL.md` nas instruções (ignore o bloco entre `---` no topo).
Se couber, cole também os arquivos de `ref/`. Prefira uma skill por projeto; para a cadeia completa, use
`texto-pronto` com `antijuridiques` e `revisor-pt-br` coladas em seguida. Nesses assistentes o `lint.py` não roda: pule o passo 3.

## Aviso

A IA erra, inclusive ao citar lei, súmula e jurisprudência com aparência de certeza. Estas skills reduzem
vícios de texto e organizam a conferência, mas não a substituem. Leia tudo, confira na fonte oficial e
assine só o que você verificou.

Licença: MIT (arquivo `LICENSE`). Use, copie e adapte à vontade, mantendo o aviso de licença.
