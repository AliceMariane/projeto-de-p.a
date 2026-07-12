from abc import ABC, abstractmethod

class Renderizador(ABC):
    '''
    Classe base para todos os renderizadores.

    Cada subclasse sabe desenhar um tipo específico
    de figura no Canvas.
    '''

    @staticmethod
    @abstractmethod
    def desenhar(canvas, figura):
        '''
        Desenha a figura
        Será implementado pelas subclasses
        '''
        pass  
    
    @staticmethod
    @abstractmethod
    def desenhar_preview(canvas, figura, dash= (4,2)):
        '''
        Preview da figura atual
        '''
        pass
