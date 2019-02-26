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
