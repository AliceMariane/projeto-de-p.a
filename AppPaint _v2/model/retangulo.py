from dataclasses import dataclass, field
from .figura import Figura


@dataclass
class Retangulo(Figura):
  '''
  Representa um retângulo desenhado pelo usuário.

  O retângulo é definido por dois vértices opostos.
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
    Inicializa o segundo vértice
    com as mesmas coordenadas do primeiro.
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
    Retorna os vértices do retângulo.
    '''

    return (
      self.ini_x,
      self.ini_y,
      self.fim_x,
      self.fim_y
    )

  def atualizar(self, x, y):
    '''
    Atualiza o segundo vértice do retângulo.
    '''

    self.fim_x = x
    self.fim_y = y

  def incompleta(self):
    '''
    Verifica se o retângulo é válido.

    O retângulo é considerado incompleto
    quando os dois vértices são iguais.
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
  
  def contorno_selecao(self, x, y):
      x_min = min(self.ini_x, self.fim_x)
      x_max = max(self.ini_x, self.fim_x)
      y_min = min(self.ini_y, self.fim_y)
      y_max = max(self.ini_y, self.fim_y)
  
      return x_min <= x <= x_max and y_min <= y <= y_max
  
