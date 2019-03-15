from fractions import Fraction
import itertools
from math import factorial

class ProbDist(dict):

    # Uma distribuição de probablidade; um mapeamento {resultado:probabilidade}

    def __init__(self, mapping=(), **kwargs):
        self.update(mapping, **kwargs)
        total = sum(self.values())
        for outcome in self:
            self[outcome] = self[outcome] / total
            assert self[outcome] >= 0

def tal_que(predicado , espaco):

    '''
    O subconjunto de elementos da colecao para os quais o predicado é verdadeiro
    Se espaco é um conjunto , retorna um subconjunto {resultado , ...}
    Se espaco é ProbDist , retorna um ProbDist{resultado , frequencia}
    '''

    if isinstance(espaco, ProbDist):
        return ProbDist({o: espaco[o] for o in espaco if predicado(o)})
    else:
        return {o for o in espaco if predicado(o)}

def P(evento , espaco):

    '''
    A probabilidade de um evento , dado um espaco amostral. evento pode ser um conjunto ou um predicado
    evento: uma coleção de resultados , ou um predicado.
    espaco: um conjunto de resultados ou a distribuicao de probabilidade na forma de pares {resultado: frequencia}.
    '''

    if callable(evento):
        evento = tal_que(evento, espaco)
    if isinstance(espaco, ProbDist):
        return sum(espaco[o] for o in espaco if o in evento)
    else:
        return Fraction(len(evento & espaco), len(espaco))

def joint(A, B, sep=''):

    '''
    A probabilidade conjunta de duas distribuições de probabilidade independentes.
    Resultado é todas as entradas da forma {a+sep+b: P(a)*P(b)}
    '''
    return ProbDist({a + sep + b: A[a] * B[b]
                     for a in A
                     for b in B})

def cross(A,B):
    
    # O conjunto de formas de concatenar os itens de A e B (produto cartesiano)"

    return {a +b
            for a in A for b in B
            }

def combos(items, n):
    # Todas as combinações de n items; cada combinação concatenada em uma string
    return{' '.join(combo)
            for combo in itertools.combinations(items,n)
            }

def escolha(n,c):

    '''
    n: tamanho da lista
    c: quantos itens da lista (tamanho da combinação)
    '''
    return factorial(n) // (factorial(c)* factorial(n - c))

