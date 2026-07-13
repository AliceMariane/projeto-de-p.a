from dataclasses import dataclass

@dataclass
class Cores:
    '''
    Armazena as cores atuais
    '''
    
    _cor_borda : str = 'black'
    _cor_preenchimento : str = ''

    @property
    def cor_borda(self):
        '''
        Retorna a cor da borda.
        '''

        return self._cor_borda
     
    @cor_borda.setter
    def cor_borda(self, cor):
        '''
        Atualiza a cor da borda.
        '''

        self._cor_borda = cor

    @property
    def cor_preenchimento(self):
        '''
        Retorna a cor do preenchimento.
        '''

        return self._cor_preenchimento

    @cor_preenchimento.setter
    def cor_preenchimento(self, cor):
        '''
        Atualiza a cor do preenchimento.
        '''

        self._cor_preenchimento = cor
