"""Testes do lint auxiliar da texto-pronto. Rodar: python -m pytest tests/"""
import importlib.util
import pathlib
import subprocess
import sys

import pytest

AQUI = pathlib.Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("lint", AQUI / "lint.py")
lint_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lint_mod)


def regras(texto):
    return [r for _, _, r in lint_mod.lint(texto)]


# --- positivos: cada frase precisa disparar a regra indicada -----------------
POSITIVOS = [
    ("Mister se faz reconhecer a prescrição.", "arcaismo"),
    ("Compulsando os autos, nada consta.", "arcaismo"),
    ("Outrossim, o prazo venceu.", "arcaismo"),
    ("Destarte, julga-se extinto.", "arcaismo"),
    ("Vimos por meio desta informar.", "arcaismo"),
    ("In casu, não houve citação.", "arcaismo"),
    ("Cabe ressaltar que o débito existe.", "vocabulario-ia"),
    ("No que tange ao prazo, nada muda.", "vocabulario-ia"),
    ("O programa atendeu mil famílias, demonstrando compromisso.", "gerundio-analise-rasa"),
    ("Houveram muitos recursos.", "haver-impessoal"),
    ("Poderiam haver outros processos.", "haver-impessoal"),
    ("Fazem 5 anos que o feito está parado.", "fazer-impessoal"),
    ("Fazem cinco anos que o feito está parado.", "fazer-impessoal"),
    ("Encaminho à Vossa Excelência o relatório.", "crase-tratamento"),
    ("Encaminho à V. Exa. o relatório.", "crase-tratamento"),
    ("A decisão implica em extinção.", "regencia-implicar"),
    ("O pedido cujo o fundamento é a prescrição.", "cujo-com-artigo"),
    ("Haja visto o exposto, indefiro.", "haja-visto-se-locucao"),
    ("A nível de município, nada muda.", "a-nivel-de"),
    ("O prazo venceu, sendo que ninguém recorreu.", "sendo-que"),
    ("Encaminharei-lhe o processo amanhã.", "enclise-futuro"),
    ("Informará-lhe o resultado.", "enclise-futuro"),
    ("Encaminharia-lhe cópia se pudesse.", "enclise-futuro"),
    ("Encaminharemos-lhe a cópia.", "enclise-futuro"),
    ("Informarão-lhe o resultado.", "enclise-futuro"),
    ("Declararei-lhe a nulidade.", "enclise-futuro"),
    ("Poderia-se evitar a prescrição.", "enclise-futuro"),
    ("Diria-lhe a verdade.", "enclise-futuro"),
    ("Deferiria-se o pedido.", "enclise-futuro"),
    ("Consideraremos-lhe o pedido.", "enclise-futuro"),
    ("Venderei-lhe o imóvel.", "enclise-futuro"),
    ("Deveriam haver outros processos.", "haver-impessoal"),
    ("O débito foi inscrito e o mesmo não foi pago.", "o-mesmo-pronome"),
    ("Recebi o ofício e respondi ao mesmo.", "o-mesmo-pronome"),
    ("## Negociações Estratégicas E Parcerias Globais", "title-case"),
    ("## Resultados Principais Obtidos Hoje", "title-case"),
    ("Lançamento previsto 🚀 para março.", "emoji"),
    ("O prazo venceu — e ninguém recorreu.", "travessao-solteiro"),
    ("O prazo venceu – e ninguém recorreu.", "travessao-solteiro"),
]


@pytest.mark.parametrize("frase,regra", POSITIVOS)
def test_positivo_dispara(frase, regra):
    assert regra in regras(frase), (frase, regras(frase))


# --- negativos: nenhuma dessas pode gerar achado -----------------------------
NEGATIVOS = [
    "O mesmo erro se repetiu em três execuções.",
    "Ao mesmo tempo, a Secretaria respondeu.",
    "O prazo é o mesmo.",
    "Peço que façam o mesmo.",
    "A mesma certidão foi juntada duas vezes.",
    "A tese — que é antiga — não procede.",
    "Houve muitos recursos.",
    "Poderia haver outros processos.",
    "Faz cinco anos que o feito está parado.",
    "Encaminho a Vossa Excelência o relatório.",
    "Levo à sua casa amanhã.",
    "A decisão implica extinção.",
    "Ele foi implicado em outro processo.",
    "O pedido cujo fundamento é a prescrição.",
    "Haja vista o exposto, indefiro.",
    "Em nível de município, nada muda.",
    "Encaminhar-lhe-ei o processo amanhã.",
    "Não lhe encaminharei o processo.",
    "Abria-se o prazo naquele dia.",
    "Queria-se evitar a prescrição.",
    "## Relatório da Secretaria de Fazenda",
    "## Prescrição intercorrente em execução fiscal",
    "## EMENTA: EXECUÇÃO FISCAL E PRESCRIÇÃO",
    "## Relatório — primeiro trimestre",
    "| Coluna | — |",
    "**[A1 — citação literal com aspas]**",
    "NOTA TÉCNICA Nº 00/0000 — COORDENADORIA",
    "— Você viu o despacho? perguntou ele.",
    "> O prazo venceu — e ninguém viu.",
    "Prazo de 5–10 dias.",
    "A análise dos autos mostra que assiste razão à parte.",
    # ênclise legítima que parece futuro, mas não é
    "Declara-se a nulidade.",
    "O débito encontra-se prescrito.",
    "Considera-se intempestivo o recurso.",
    "Varia-se o índice.",
    "Adquiria-se o imóvel naquela época.",
    "Declarei-lhe a nulidade na audiência.",
    "Considerei-o intempestivo.",
    "Cria-se a comissão.",
    # a família inteira, não só as palavras citadas
    "Atirei-lhe o documento.", "Encarei-o de frente.", "Mirei-o com atenção.",
    "Exagerei-o no relatório.", "Onerei-o com a taxa.", "Aparei-o nas bordas.",
    "Suspirei-lhe a resposta.", "Prosperei-me no cargo.", "Apoderei-me do bem.",
    "Retirei-o dos autos.", "Recuperei-o no sistema.",
    "Diferia-se o pagamento.", "Auferia-se renda do imóvel.",
    "Preteria-se o credor.", "Desferia-se o golpe.", "Vangloria-se do feito.",
    "Encarcerei-o ontem.", "Asseverei-lhe a verdade.", "Peneirei-os um a um.",
    "O empregador assalaria-se de outro modo.",
    "Conferia-se a certidão.", "Proferia-se a decisão.", "Sugeria-se o acordo.",
    "Transferia-se o crédito.", "Inseria-se a cláusula.",
    # tempo composto de haver
    "Podem haver sido extintos os créditos.",
]


@pytest.mark.parametrize("frase", NEGATIVOS)
def test_negativo_sem_falso_positivo(frase):
    assert lint_mod.lint(frase) == [], (frase, lint_mod.lint(frase))


# --- bordas -------------------------------------------------------------------
def test_texto_vazio():
    assert lint_mod.lint("") == []


def test_bloco_de_codigo_ignorado():
    texto = "```\nHouveram erros — no log.\n```\nTexto limpo."
    assert lint_mod.lint(texto) == []


def test_travessao_par_em_frases_distintas_nao_e_par():
    # um travessão em cada frase: dois solteiros, não um par
    texto = "O prazo venceu — sem aviso. A parte recorreu — tarde demais."
    assert regras(texto).count("travessao-solteiro") == 2


def test_numero_de_linha_correto():
    texto = "Linha limpa.\n\nOutrossim, segue."
    assert lint_mod.lint(texto)[0][0] == 3


def test_varios_achados_na_mesma_linha():
    r = regras("Outrossim, houveram falhas, sendo que ninguém viu.")
    assert {"arcaismo", "haver-impessoal", "sendo-que"} <= set(r)


# --- ponto de entrada (CLI) -----------------------------------------------------
def _rodar(args, entrada=None):
    return subprocess.run(
        [sys.executable, str(AQUI / "lint.py"), *args],
        input=entrada, capture_output=True, text=True,
    )


def test_cli_arquivo(tmp_path):
    arq = tmp_path / "t.md"
    arq.write_text("Texto limpo.\nHouveram falhas.\n", encoding="utf-8")
    r = _rodar([str(arq)])
    assert r.returncode == 0
    linhas = r.stdout.strip().splitlines()
    assert linhas[0].startswith("2:") and linhas[0].endswith(":haver-impessoal")
    assert linhas[-1] == "1 achados"


def test_cli_stdin():
    r = _rodar(["-"], entrada="Mister se faz agir.\n")
    assert r.returncode == 0
    assert ":arcaismo" in r.stdout


def test_cli_arquivo_inexistente_sai_zero_com_erro_visivel(tmp_path):
    r = _rodar([str(tmp_path / "nao-existe.md")])
    assert r.returncode == 0
    assert "ERRO" in r.stdout


def test_cli_texto_limpo():
    r = _rodar([], entrada="Texto sem problema nenhum.\n")
    assert r.returncode == 0
    assert r.stdout.strip() == "0 achados"
