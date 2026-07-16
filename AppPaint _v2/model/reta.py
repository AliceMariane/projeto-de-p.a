from dataclasses import dataclass, field
from .figura import Figura
import math


@dataclass
class Reta(Figura):
  '''
  Representa uma reta desenhada pelo usuário.

  O primeiro click do mouse define o ponto inicial,
  o ponto final começa igual ao ponto inicial.
  '''

  # Primeiro Vértice (x, y)
  _ini_x: int
  _ini_y: int

  cor_borda: str ='black'
  cor_preenchimento: str = 'white'
  
  # Segundo Vértice (x, y)
  _fim_x: int = field(init=False)
  _fim_y: int = field(init=False)

  def __post_init__(self):
    '''
    Inicializa o ponto final da reta
    com as mesmas coordenadas do ponto inicial.
    '''

    self.fim_x = self.ini_x
    self.fim_y = self.ini_y

  @property
  def ini_x(self):
    '''
    Retorna a coordenada x do ponto inicial.
    '''

    return self._ini_x

  @ini_x.setter
  def ini_x(self, valor):
    '''
    Atualiza a coordenada x do ponto inicial.
    '''

    self._ini_x = valor

  @property
  def ini_y(self):
    '''
    Retorna a coordenada y do ponto inicial.
    '''

    return self._ini_y

  @ini_y.setter
  def ini_y(self, valor):
    '''
    Atualiza a coordenada y do ponto inicial.
    '''

    self._ini_y = valor

  @property
  def fim_x(self):
    '''
    Retorna a coordenada x do ponto final.
    '''

    return self._fim_x

  @fim_x.setter
  def fim_x(self, valor):
    '''
    Atualiza a coordenada x do ponto final.
    '''

    self._fim_x = valor

  @property
  def fim_y(self):
    '''
    Retorna a coordenada y do ponto final.
    '''

    return self._fim_y

  @fim_y.setter
  def fim_y(self, valor):
    '''
    Atualiza a coordenada y do ponto final.
    '''

    self._fim_y = valor

  @property
  def pontos(self):
    '''
    Retorna os vértices da reta.
    '''

    return (
      self.ini_x,
      self.ini_y,
      self.fim_x,
      self.fim_y
    )

  def atualizar(self, x, y):
    '''
    Atualiza o último ponto (x, y) da reta.
    '''

    self.fim_x = x
    self.fim_y = y

  def incompleta(self):
    '''
    Verifica se a reta é válida.

    Uma reta é considerada incompleta
    quando os pontos são iguais.
    '''

    return (
      self.ini_x == self.fim_x and
      self.ini_y == self.fim_y
    )

  def mover(self, d_x, d_y):
      self.ini_x += d_x
      self.ini_y += d_y
      self.fim_x += d_x
      self.fim_y += d_y

  def contem_ponto(self, x, y, tolerancia=5):
        px = self.fim_x - self.ini_x
        py = self.fim_y - self.ini_y
        somados_quadrados = px**2 + py**2
        
        if somados_quadrados == 0:
            return math.sqrt((x - self.ini_x)**2 + (y - self.ini_y)**2) <= tolerancia

        u = ((x - self.ini_x) * px + (y - self.ini_y) * py) / float(somados_quadrados)

        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        x_proximo = self.ini_x + u * px
        y_proximo = self.ini_y + u * py

        dx = x_proximo - x
        dy = y_proximo - y

        distancia = math.sqrt(dx**2 + dy**2)
        return distancia <= tolerancia
  
  def contorno_selecao(self, x, y):
      x_min = min(self.ini_x, self.fim_x)
      x_max = max(self.ini_x, self.fim_x)
      y_min = min(self.ini_y, self.fim_y)
      y_max = max(self.ini_y, self.fim_y)
  
      return x_min <= x <= x_max and y_min <= y <= y_max
  
