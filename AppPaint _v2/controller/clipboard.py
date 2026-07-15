from dataclasses import dataclass
import copy
from model.figura import Figura


@dataclass
class Clipboard:
    '''
    Responsável pela área de transferência do Paint

    Armazena uma cópia da figura selecionada,
    permitindo copiá-la e colá-la posteriormente
    '''

    _figura: Figura | None = None

    def copiar(self, figura: Figura | None):
        '''
        Armazena uma cópia da figura selecionada.
        '''

        if figura is None:
            return

        self._figura = copy.deepcopy(figura)

    def colar(self) -> Figura | None:
        '''
        Retorna uma cópia da figura armazenada
        '''

        if self._figura is None:
            return None

        nova_figura = copy.deepcopy(self._figura)

        # move um pouco para não sobrepor
        nova_figura.mover(20, 20)

        return nova_figura

    def limpar(self):
        '''
        Remove a figura armazenada da área de transferência
        '''

        self._figura = None