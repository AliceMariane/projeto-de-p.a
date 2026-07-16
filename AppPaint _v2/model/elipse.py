from dataclasses import dataclass, field
from .figura import Figura


@dataclass
class Elipse(Figura):
  '''
  Representa uma elipse.

  A elipse é construída a partir do retângulo
  delimitador formado por dois vértices opostos.

  Esses vértices são definidos pelo clique
  inicial e pela posição atual do mouse.
  '''

  # Primeiro Vértice do retângulo delimitador (x, y)
  _ini_x: int
  _ini_y: int

  cor_borda: str ='black'
  cor_preenchimento: str = 'white'

  # Segundo Vértice do retângulo delimitador (x, y)
  _fim_x: int = field(init=False)
  _fim_y: int = field(init=False)

  def __post_init__(self):
    '''
    Começa o segundo ponto do retângulo delimitador
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
    Retorna os vértices do retângulo delimitador.
    '''

    return (
      self.ini_x,
      self.ini_y,
      self.fim_x,
      self.fim_y
    )

  def atualizar(self, x, y):
    '''
    Atualiza o segundo vértice do retângulo
    delimitador da elipse.
    '''

    self.fim_x = x
    self.fim_y = y

  def incompleta(self):
    '''
    Verifica se a elipse pode ser criada.

    A elipse é inválida quando
    os dois vértices são iguais.
    '''

    return not self._figura_valida()

  def _figura_valida(self, minimo=5):
    '''
    Evita fazer a elipse se comportar como reta.
    '''

    largura = abs(self.fim_x - self.ini_x)
    altura = abs(self.fim_y - self.ini_y)

    return (
      largura >= minimo and
      altura >= minimo
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
    def contem_ponto(self, x, y):
    #Pontos externos
    x_min, x_max = min(self.x1, self.x2), max(self.x1, self.x2)
    y_min, y_max = min(self.y1, self.y2), max(self.y1, self.y2)
    # Centros
    xc = (x_min + x_max)/2
    yc = (y_min + y_max)/2
    #Raios
    a = (x_max - x_min)/2
    b = (y_max - y_min)/2

    if a == 0 or b == 0:
        return False
    return ((x - xc) **2) / (a**2) + ((y - yc)**2)/(b**2 <=1)
