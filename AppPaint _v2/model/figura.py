from abc import ABC, abstractmethod, dataclasses
from dataclasses import dataclass, field

@dataclass
class Figura(ABC):
    '''
    Classe abstrata base para todas as figuras.
    '''

    _cor_borda : str = "black"
    _cor_preenchimento : str = ""

    @abstractmethod
    def atualizar(self, x, y):
        '''
        Atualiza o ultimo ponto (x, y) da figura
        Será implementado pelas subclasses
        '''
        pass

    @abstractmethod
    def desenhar(self, canvas):
        '''
        Desenha a figura
        Será implementado pelas subclasses
        '''
        pass

    @abstractmethod
    def desenhar_preview(self, canvas):
        '''
        Preview da figura atual
        '''
        pass

    @abstractmethod
    def incompleta(self):
        '''
        Verifica se a figura pode ser salva
        '''
        pass
    
