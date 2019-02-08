from fractions import Fraction

class ProbDist(dict):
    def __init__(self, mapping=(), **kwargs):
        self.update(mapping, **kwargs)
        total = sum(self.values())
        for outcome in self:
            self[outcome] = self[outcome] / total
            assert self[outcome] >= 0

#Metodo remoção da pergunta, nas listas de possiveis respostas
def limpaInicio(a):
    a.remove(a[0])
    return a

def tal_que(predicado , espaco):
    if isinstance(espaco, ProbDist):
        return ProbDist({o: espaco[o] for o in espaco if predicado(o)})
    else:
        return {o for o in espaco if predicado(o)}

def P(evento , espaco):
    if callable(evento):
        evento = tal_que(evento, espaco)
    if isinstance(espaco, ProbDist):
        return sum(espaco[o] for o in espaco if o in evento)
    else:
        return Fraction(len(evento & espaco), len(espaco))

def joint(A, B, sep=''):
    return ProbDist({a + sep + b: A[a] * B[b]
                     for a in A
                     for b in B})


base = open("123.csv", "r")
base1 = base.read()
splitln = base1.split("\n")
splitln.remove(splitln[-1])

# Declaração Variaveis
splitVar = []
array_ensino = []
array_frequencia = []
array_ferramenta = []
array_problemas = []
array_sugestao = []
#Ajuste na base para conseguir extrair as informações.
for string in splitln:
    split = string.replace('"""', "")
    splitVar.append(split.split('"'))

#Preenchimento das listas com as possiveis respostas do questionario.
for j in splitVar:
    for ferramenta in j[8].split(','):
        array_ferramenta.append(ferramenta.lower())
    for ensino in j[0].split(','):
        array_ensino.append(ensino.lower())
    for frequencia in j[4].split(','):
        array_frequencia.append(frequencia.lower())
    for problemas in j[12].split(','):
        array_problemas.append(problemas.lower())
    for sugestao in j[12].split(','):
        array_sugestao.append(sugestao.lower())

#Removendo Questionario das possiveis respostas
limpaInicio(array_ensino)
limpaInicio(array_frequencia)
limpaInicio(array_ferramenta)
limpaInicio(array_problemas)
limpaInicio(array_sugestao)


PEnsino = ProbDist(
    Medio_completo = array_ensino.count("ensino médio completo"),
    Superior_incompleto = array_ensino.count("ensino superior incompleto"),
    Superior_completo = array_ensino.count("ensino superior completo"),
    Pos_graduacao = array_ensino.count("pós-graduação"),
)

PFrequencia = ProbDist(
    Moderada = array_frequencia.count("moderada"),
    Nenhuma = array_frequencia.count("nenhuma"),
    Pouca = array_frequencia.count("pouca"),
    Intensa = array_frequencia.count("intensa"),
)

PFerramenta = ProbDist(
    Google = array_ferramenta.count("google docs"),
    Word = array_ferramenta.count("word"),
    Libre_office = array_ferramenta.count("libre office"),
    One_note = array_ferramenta.count("onenote"),
    Latex = array_ferramenta.count("latex"),
    Only_office = array_ferramenta.count("only office"),
    Bloco_notas = array_ferramenta.count("bloco de notas"),
    Share_latex = array_ferramenta.count("sharelatex"),
    Fast_format = array_ferramenta.count("fast format"),
    Quip = array_ferramenta.count("quip"),
    Zoho = array_ferramenta.count("zoho"),
    Overleaf = array_ferramenta.count("overleaf"),
)

PProblemas = ProbDist(
    NumPags = array_problemas.count("numeração de páginas"),
    ConfFerramenta = array_problemas.count("difícil configuração da ferramenta para as normas que exigem do trabalho"),
    Alinhamento_texto = array_problemas.count("alinhamento do texto"),
    Chato_docs_word = array_problemas.count("mas consideremo mais chato fazer isso em ferramentas como google docs e word."),
    Comecar_trabalho = array_problemas.count("começar o trabalho"),
    Escrita_texto = array_problemas.count("escrita do texto"),
    Fazer_citacoes = array_problemas.count("fazer citações"),
    Criar_referencias = array_problemas.count("criar referências"),
    Nao_sei = array_problemas.count("não sei"),
    Modelo_Documento = array_problemas.count("procurar um modelo de documento"),
    Lista_figuras = array_problemas.count("criação de lista de figuras"),
    Layout_latex = array_problemas.count("certas dificuldades em ajustar um layout em latex de uma determinada conferência ou instituição de ensino."),
    Nenhum = array_problemas.count("nenhum"),
    Um_pouco_cada = array_problemas.count("um pouco de cada"),
    Criar_tabelas = array_problemas.count("criar tabelas"),
    Depende_ferramenta = array_problemas.count("depende da ferramenta a ser utilizada e meu nível de conhecimento"),
    Criacao_sumarios = array_problemas.count("criação de sumários"),
    Nenhuma_opcoes = array_problemas.count("nenhuma das opções"),
    Espacamento_texto = array_problemas.count("espaçamento do texto"),
    Nao_compreender_ferramenta = array_problemas.count("não compreender a ferramenta"),
    Criacao_template = array_problemas.count("criação de template qdo ainda não existe pronto"),
)

PSugestoes = ProbDist(
    Criacao_lista_figuras = array_sugestao.count("criação de lista de figuras"),
    Criacao_template = array_sugestao.count("criação de template qdo ainda não existe pronto"),
    Comecar_trabalho = array_sugestao.count("começar o trabalho"),
    Modelo_documento = array_sugestao.count("procurar um modelo de documento"),
    Escrita_texto = array_sugestao.count("escrita do texto"),
    Criar_tabelas = array_sugestao.count("criar tabelas"),
    Nenhum = array_sugestao.count("nenhum"),
    Nenhuma = array_sugestao.count("nenhuma das opções"),
    Sumario = array_sugestao.count("criação de sumários"),
    Espacamento_texto = array_sugestao.count("espaçamento do texto"),
    Criar_referencia = array_sugestao.count("criar referências"),
    Fazer_citacoes = array_sugestao.count("fazer citações"),
)
