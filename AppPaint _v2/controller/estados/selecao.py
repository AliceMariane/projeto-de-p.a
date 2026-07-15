from dataclasses import dataclass

from model.figura import Figura


@dataclass
class Selecao:
    '''
    Gerencia a figura atualmente selecionada.
    '''

    figura: Figura | None = None

    def selecionar(self, figura: Figura | None):
        '''
        Define uma figura como selecionada.
        '''

        self.figura = figura

    def limpar(self):
        '''
        Remove a seleção atual.
        '''

        self.figura = None

    def existe(self) -> bool:
        '''
        Verifica se existe alguma figura selecionada.
        '''

        return self.figura is not None