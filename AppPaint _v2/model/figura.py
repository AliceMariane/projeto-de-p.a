from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Figura(ABC):
    '''
    Classe abstrata base para todas as figuras.
    
    Cada figura é responsável apenas por armazenar seus
    próprios dados geométricos.

    O desenho da figura é realizado pelos renderizadores.
    '''

    @abstractmethod
    def atualizar(self, x, y):
        '''
        Atualiza o ultimo ponto (x, y) da figura
        Será implementado pelas subclasses
        '''
        pass

    @abstractmethod
    def incompleta(self):
        '''
        Verifica se a figura pode ser salva
        '''
        pass

    @abstractmethod
    def mover(self, d_x, d_y):
        '''
        Mover a figura
        '''
        pass

    @abstractmethod
    def contorno_selecao(self, x, y):
        '''Verifica se forma o contorno
        '''
        pass
        
    @abstractmethod
    def contem_ponto(self, x, y):
        pass

