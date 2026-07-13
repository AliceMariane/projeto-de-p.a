from abc import ABC, abstractmethod


class Renderizador(ABC):
  '''
  Classe base para todos os renderizadores.

  Cada subclasse sabe desenhar um tipo específico
  de figura no Canvas.
  '''

  @staticmethod
  @abstractmethod
  def desenhar(canvas, figura, cores):
    '''
    Desenha definitivamente uma figura.
    '''

    pass

  @staticmethod
  @abstractmethod
  def desenhar_preview(canvas, figura, cores, dash=(4, 2)):
    '''
    Desenha o preview da figura.
    '''

    pass
