#!/usr/bin/env python3
"""Lint auxiliar da cadeia texto-pronto (stdlib apenas).

Uso:  python3 lint.py ARQUIVO      |  ... | python3 lint.py [-]

Saída: uma linha por achado, "linha:trecho:regra", e no fim "N achados".
Sempre sai com código 0: é auxiliar, não portão. Achado é CANDIDATO; quem
decide é o julgamento da skill (zona intocável, sentido, registro).

Não olha linhas de citação em bloco (">") nem blocos de código (```), que
costumam ser zona intocável.
"""
import re
import sys

PRONOMES = r"(?:me|te|se|lhe|lhes|nos|vos|o|a|os|as|lo|la|los|las)"

# (regra, regex) — casamento insensível a maiúsculas.
FRASES = [
    # arcaísmo e fórmula vazia (tabela da antijuridiques)
    ("arcaismo", r"\bmister se faz\b"),
    ("arcaismo", r"\bcompulsando os autos\b"),
    ("arcaismo", r"\bpetit[óo]rio vestibular\b"),
    ("arcaismo", r"\bexordial\b"),
    ("arcaismo", r"\boutrossim\b"),
    ("arcaismo", r"\bdestarte\b"),
    ("arcaismo", r"\bdessarte\b"),
    ("arcaismo", r"\bpor derradeiro\b"),
    ("arcaismo", r"\bmalgrado\b"),
    ("arcaismo", r"\bconsoante o entendimento\b"),
    ("arcaismo", r"\bab initio\b"),
    ("arcaismo", r"\bdata maxima venia\b"),
    ("arcaismo", r"\bperlustrando\b"),
    ("arcaismo", r"\bpe[çc]a incoativa\b"),
    ("arcaismo", r"\besposar o entendimento\b"),
    ("arcaismo", r"\bcarread[oa]s? aos autos\b"),
    ("arcaismo", r"\bin casu\b"),
    ("arcaismo", r"\b(?:vimos|venho) por meio\b"),
    # vocabulário de IA (subconjunto seguro)
    ("vocabulario-ia", r"\bcabe ressaltar\b"),
    ("vocabulario-ia", r"\b[ée] importante salientar\b"),
    ("vocabulario-ia", r"\bvale destacar\b"),
    ("vocabulario-ia", r"\bcen[áa]rio em constante evolu[çc][ãa]o\b"),
    ("vocabulario-ia", r"\bnesse sentido\b"),
    ("vocabulario-ia", r"\bsob essa [óo]tica\b"),
    ("vocabulario-ia", r"\bno que tange\b"),
    ("vocabulario-ia", r"(?<!\w)[àa] luz d[eoa]s?\b"),
    ("gerundio-analise-rasa",
     r",\s*(?:demonstrando|evidenciando|garantindo|ressaltando|destacando"
     r"|refletindo|simbolizando|enfatizando)\b"),
    # erros de norma frequentes
    ("haver-impessoal", r"\bhouveram\b"),
    ("haver-impessoal",
     r"\b(?:podem|poderiam|poder[ãa]o|devem|deveriam|dever[ãa]o|v[ãa]o|iriam|costumam)\s+haver\b"
     r"(?!\s+(?:sido|tido|feito|havido|estado|ocorrido|\w+ado|\w+ido)\b)"),
    ("fazer-impessoal",
     r"\b(?:fazem|faziam|fizeram)\s+(?:\d+|dois|duas|tr[êe]s|quatro|cinco|seis|sete|oito"
     r"|nove|dez|v[áa]rios|v[áa]rias|muitos|muitas|alguns|algumas)\s+"
     r"(?:anos|meses|dias|semanas|horas|d[ée]cadas)\b"),
    ("crase-tratamento",
     r"(?<!\w)[àÀ]\s+(?:Vossa\b|V\.\s*(?:Exa|Ex\.?ª|Sa|S\.?ª)|Sua\s+(?:Excel[êe]ncia|Senhoria"
     r"|Santidade|Majestade|Alteza|Emin[êe]ncia|Magnific[êe]ncia))"),
    ("regencia-implicar",
     r"\bimplic(?:a|am|ava|avam|ou|aram|ar[áa]|ar[ãa]o|aria|ariam|ar)\s+em\b"),
    ("cujo-com-artigo", r"\bcuj(?:o\s+o|a\s+a|os\s+os|as\s+as)\b"),
    # só a locução "haja visto" (= considerando) é erro; tempo composto de
    # "ver" ("embora o juiz haja visto os autos") é correto: julgue pelo sentido
    ("haja-visto-se-locucao", r"\bhajam?\s+visto\b"),
    ("a-nivel-de", r"(?<!\w)[àa]\s+n[íi]vel\s+de\b"),
    ("sendo-que", r"\bsendo\s+que\b"),
]
FRASES = [(r, re.compile(p, re.IGNORECASE)) for r, p in FRASES]

# Ênclise no futuro do presente / do pretérito: "encaminharei-lhe", "faria-se".
# rá/rás/rão só com acento (sem acento é presente: "declara-se", "encontra-se").
ENCLISE_FUTURO = re.compile(
    r"\b(\w+?)(rei|rás|rá|remos|reis|rão|ria|rias|ríamos|ríeis|riam)-"
    + PRONOMES + r"\b",
    re.IGNORECASE,
)
# Futuro do pretérito ("-ria") x imperfeito/presente, por FAMÍLIA do radical
# (radical = palavra sem "-ria/-rias/-riam/-ríamos/-ríeis"):
#   ...fe/...ge/...que  -> imperfeito de -ferir/-gerir/-querer (auferia, sugeria,
#                          queria): não existe infinitivo "-fer/-ger/-quer"
#   ...qui              -> imperfeito de -quirir (adquiria, inquiria)
#   ...o (exceto ...po) -> presente de -oriar (vangloria); "poria" é pôr
#   consoante           -> imperfeito/presente (abria, cria)
# e poucos isolados que a família não resolve (preteria, inseria, aderia, varia).
SUFIXO_NAO_CONDICIONAL = ("fe", "ge", "que", "qui")
RADICAL_NAO_CONDICIONAL = {"prete", "inse", "ade", "va", "contra", "ava", "desva", "assala"}


def _eh_condicional(radical):
    if not radical or radical[-1] not in "aeioôê":
        return False
    if radical.endswith(SUFIXO_NAO_CONDICIONAL) or radical in RADICAL_NAO_CONDICIONAL:
        return False
    if radical[-1] in "oô" and not radical.endswith(("po", "pô")):
        return False
    return True


# Futuro do presente em "-rei/-remos/-reis" colide com pretérito/subjuntivo de
# verbo em -Vrar (declarei, atirei, declaremos). Sem dicionário não há regra
# morfológica que separe "considerei" de "responderei"; fica a lista dos -arar,
# -erar e -irar comuns. "-VrVrei" (declararei) é sempre futuro.
_VERBOS_RAR = (
    "aclarar amparar aparar comparar declarar deparar desamparar disparar "
    "encarar equiparar escancarar parar preparar reparar separar varar "
    "encarcerar asseverar peneirar "
    "acelerar adulterar alterar apoderar atemperar comiserar considerar "
    "cooperar degenerar deliberar desesperar desonerar dilacerar enumerar "
    "esmerar esperar exagerar exasperar exonerar gerar imperar lacerar liberar "
    "moderar numerar obliterar onerar operar perseverar ponderar preponderar "
    "prosperar reconsiderar recuperar regenerar reiterar remunerar reverberar "
    "superar temperar tolerar venerar vociferar zerar "
    "admirar aspirar atirar conspirar delirar estirar expirar girar inspirar "
    "mirar respirar retirar revirar suspirar tirar transpirar virar "
    "abeirar cheirar inteirar"
).split()
NAO_FUTURO_REI = {v[:-2] + t for v in _VERBOS_RAR for t in ("ei", "emos", "eis")}
NAO_FUTURO_REI |= {"queremos", "requeremos", "quereis", "requereis"}

# "o mesmo" como pronome: seguido de verbo/negação/pontuação.
MESMO = re.compile(
    r"\b(?:o|a|os|as|do|da|dos|das|no|na|nos|nas|ao|aos|pelo|pela|pelos|pelas)"
    r"\s+mesm(?:o|a|os|as)\b(?P<depois>\s*(?:[.,;:)!?]|$|\w+))",
    re.IGNORECASE,
)
MESMO_SEGUINTE_PRONOMINAL = {
    "não", "se", "já", "foi", "é", "era", "será", "seria", "está", "estava",
    "esteve", "estará", "tem", "tinha", "teve", "terá", "deve", "devia",
    "deverá", "pode", "podia", "poderá", "possui", "foram", "são", "eram",
    "serão", "estão", "estavam", "têm", "tinham", "devem", "podem", "também",
    "ainda", "nunca", "jamais", "sempre", "lhe", "lhes", "encontra",
    "encontram", "apresenta", "apresentou", "informou", "alegou", "requereu",
}
MESMO_ANTES_LEGITIMO = re.compile(
    r"\b(?:é|era|foi|será|seria|seja|são|eram|foram|continua|permanece|fica"
    r"|faz|fez|fazer|faça|façam|fará|faria|fazem|fizeram|mais)\s*$",
    re.IGNORECASE,
)

TRAVESSAO = re.compile(r"—|\s–\s")
FIM_DE_FRASE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÀÇ\"“(])")

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U0001F1E6-\U0001F1FF\U00002600-\U000027BF"
    "\U00002B50\U00002B55\U0001F000-\U0001F2FF]"
)

FUNCIONAIS = {
    "e", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "para", "com", "a", "o", "os", "as", "ou", "por", "ao", "aos", "à", "às",
}


def _trecho(texto, ini, fim, folga=20):
    a = max(0, ini - folga)
    b = min(len(texto), fim + folga)
    s = texto[a:b].strip().replace("\n", " ")
    return ("…" if a > 0 else "") + s + ("…" if b < len(texto) else "")


def _title_case(titulo):
    palavras = re.findall(r"[\wÀ-ÿ-]+", titulo)
    if len(palavras) < 2:
        return False
    letras = [c for c in titulo if c.lower() != c.upper()]
    if letras and all(c.isupper() for c in letras):
        return False  # caixa alta inteira: ementa/transcrição, não Title Case
    resto = palavras[1:]
    for p in resto:
        sigla = len(p) > 1 and p.isupper()
        if p.lower() in FUNCIONAIS and p[0].isupper() and not sigla:
            return True  # "Parcerias E Metas", "Análise Da Prescrição"
    conteudo = [p for p in resto if len(p) >= 4 and p.lower() not in FUNCIONAIS]
    maiusc = [p for p in conteudo if p[0].isupper()]
    return len(maiusc) >= 3 and len(maiusc) / len(conteudo) >= 0.75


def lint(texto):
    """Devolve lista de (linha, trecho, regra)."""
    achados = []
    em_codigo = False
    linhas = texto.splitlines()
    for n, linha in enumerate(linhas, 1):
        crua = linha.strip()
        if crua.startswith("```"):
            em_codigo = not em_codigo
            continue
        if em_codigo or crua.startswith(">") or not crua:
            continue

        if crua.startswith("#"):
            titulo = crua.lstrip("#").strip()
            if _title_case(titulo):
                achados.append((n, titulo, "title-case"))
            for m in EMOJI.finditer(linha):
                achados.append((n, _trecho(linha, m.start(), m.end()), "emoji"))
            continue  # travessão em título é separador legítimo

        for regra, rx in FRASES:
            for m in rx.finditer(linha):
                achados.append((n, _trecho(linha, m.start(), m.end()), regra))

        for m in ENCLISE_FUTURO.finditer(linha):
            radical, sufixo = m.group(1).lower(), m.group(2).lower()
            palavra = (radical + sufixo)
            if sufixo.startswith("ria") or sufixo.startswith("rí"):
                if not _eh_condicional(radical):
                    continue  # auferia-se, adquiria-se, vangloria-se, abria-se
            elif sufixo in ("rei", "remos", "reis"):
                if not radical or radical[-1] not in "aeiô" and not radical.endswith("po"):
                    continue  # mostrei, apurei, ignorei: pretérito
                if palavra in NAO_FUTURO_REI:
                    continue  # declarei-lhe, considerei-o: pretérito
            achados.append((n, _trecho(linha, m.start(), m.end()), "enclise-futuro"))

        for m in MESMO.finditer(linha):
            depois = m.group("depois").strip().lower()
            if depois and depois[0].isalnum() and depois not in MESMO_SEGUINTE_PRONOMINAL:
                continue  # "o mesmo erro", "ao mesmo tempo"
            if MESMO_ANTES_LEGITIMO.search(linha[: m.start()]):
                continue  # "é o mesmo", "fazer o mesmo"
            achados.append((n, _trecho(linha, m.start(), m.end()), "o-mesmo-pronome"))

        for m in EMOJI.finditer(linha):
            achados.append((n, _trecho(linha, m.start(), m.end()), "emoji"))

        if crua.startswith("|"):
            continue  # tabela: "—" é célula vazia
        letras = [c for c in crua if c.lower() != c.upper()]
        if (crua.startswith("**") and crua.endswith("**")) or (
                letras and all(c.isupper() for c in letras)):
            continue  # rótulo em negrito ou cabeçalho em caixa alta: separador
        corpo = re.sub(r"^\s*(?:[-*+]|\d+[.)])?\s*[—–]\s*", "", linha)  # diálogo/marcador
        for frase in FIM_DE_FRASE.split(corpo):
            marcas = list(TRAVESSAO.finditer(frase))
            if len(marcas) % 2 == 1:
                ult = marcas[-1]
                achados.append(
                    (n, _trecho(frase, ult.start(), ult.end()), "travessao-solteiro"))
    return achados


def main(argv):
    try:
        if len(argv) > 1 and argv[1] != "-":
            with open(argv[1], encoding="utf-8", errors="replace") as f:
                texto = f.read()
        else:
            texto = sys.stdin.read()
    except OSError as e:
        print(f"lint: ERRO ao ler entrada ({e.strerror}); siga sem o lint")
        return 0
    achados = lint(texto)
    for n, trecho, regra in achados:
        print(f"{n}:{trecho}:{regra}")
    print(f"{len(achados)} achados")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
