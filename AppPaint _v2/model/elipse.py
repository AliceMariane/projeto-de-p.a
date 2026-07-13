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
