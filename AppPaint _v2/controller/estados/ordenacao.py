from model.figura import Figura


class Ordenacao:
    '''
    Responsável pela ordem das figuras no desenho
    '''

    def frente(self, figuras: list[Figura], figura: Figura):
        '''
        Move a figura uma posição para frente
        '''

        if figura not in figuras:
            return

        indice = figuras.index(figura)

        if indice < len(figuras) - 1:
            figuras[indice], figuras[indice + 1] = (
                figuras[indice + 1],
                figuras[indice]
            )

    def tras(self, figuras: list[Figura], figura: Figura):
        '''
        Move a figura uma posição para trás
        '''

        if figura not in figuras:
            return

        indice = figuras.index(figura)

        if indice > 0:
            figuras[indice], figuras[indice - 1] = (
                figuras[indice - 1],
                figuras[indice]
            )

    def topo(self, figuras: list[Figura], figura: Figura):
        '''
        Move a figura para o topo da pilha
        '''

        if figura not in figuras:
            return

        figuras.remove(figura)
        figuras.append(figura)

    def fundo(self, figuras: list[Figura], figura: Figura):
        '''
        Move a figura para o fundo da pilha
        '''

        if figura not in figuras:
            return

        figuras.remove(figura)
        figuras.insert(0, figura)