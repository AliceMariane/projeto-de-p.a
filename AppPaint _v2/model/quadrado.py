from dataclasses import dataclass, field
from .figura import Figura

@dataclass
class Quadrado(Figura):
  '''
  Representa um quadrado desenhado pelo usuário.

  O quadrado é criado a partir de dois pontos:
  
  O primeiro vértice é definido quando o usuário
  pressiona o botão do mouse.

  O segundo vértice acompanha o movimento do
  mouse enquanto o botão estiver pressionado.
  '''
  
  # Primeiro Vértice (x, y)
  _ini_x : int
  _ini_y : int
  
  # Segundo Vértice (x, y)
  _fim_x : int = field(init= False)
  _fim_y : int = field(init= False)  
  
  def __post_init__(self):
    '''
    Começa o ultimo ponto do quadrado 
    com as mesmas coordenadas do primeiro
    '''
    
    self._fim_x = self._ini_x
    self._fim_y = self._ini_y
    
  @property
  def pontos(self):
    '''
    Retorna os vértices do quadrado.
    '''
    
    return (
      self._ini_x,
      self._ini_y,
      self._fim_x,
      self._fim_y
    )
  
  @property
  def ini_x(self):
    return self._ini_x
  
  @property
  def ini_y(self):
    return self._ini_y
  
  @property
  def fim_x(self):
    return self._fim_x
  
  @property
  def fim_y(self):
    return self._fim_y
    
  def atualizar(self, x, y):
    '''
    Atualiza o ultimo vértice (x, y) do quadrado,
    ajustando a largura e a altura para manter os lados iguais
    '''
    
    dx = x - self.ini_x
    dy = y - self.ini_y
    
    lado = max(abs(dx), abs(dy))
    self._fim_x = self.ini_x + (lado if dx >= 0 else -lado)
    self._fim_y = self.ini_y + (lado if dy >= 0 else -lado)

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva o quadrado na tela
    '''
    
    canvas.create_rectangle(*self.pontos, 
                            outline= self._cor_borda, 
                            fill= self._cor_preenchimento)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado do quadrado em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_rectangle(*self.pontos, 
                            outline= self._cor_borda, 
                            fill= self._cor_preenchimento,
                            dash= (4, 2))

  def incompleta(self):
    '''
    Verifica se o quadrado foi desenhado corretamente.
    '''
    
    return (abs(self.fim_x - self.ini_x) == 0 and
            abs(self.fim_y - self.ini_y) == 0
      )
