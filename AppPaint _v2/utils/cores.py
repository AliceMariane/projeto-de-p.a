from dataclasses import dataclass

@dataclass
class Cores:
    _cor_borda : str = 'black'
    _cor_preenchimento : str = ''

    @property
    def cor_borda(self):
        '''
        Retorna a cor da borda.
        '''

        return self._cores.borda
     
    @cor_borda.setter
    def cor_borda(self, cor):
        '''
        Atualiza a cor da borda.
        '''

        self._cores.borda = cor

    @property
    def cor_preenchimento(self):
        '''
        Retorna a cor do preenchimento.
        '''

        return self._cores.preenchimento

    @cor_preenchimento.setter
    def cor_preenchimento(self, cor):
        '''
        Atualiza a cor do preenchimento.
        '''

        self._cores.preenchimento = cor
