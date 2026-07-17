from dataclasses import dataclass, field
from .figura import Figura
import math


@dataclass
class Circulo(Figura):
  '''
  Representa um círculo desenhado pelo usuário.

  Enquanto o usuário arrasta o mouse,
  o raio é recalculado em tempo real utilizando
  a distância entre o centro e a posição atual do mouse.
  '''

  _cx: int
  _cy: int

  cor_borda: str ='black'
  cor_preenchimento: str = 'white'

  _raio: float = field(init=False)

  def __post_init__(self):
    '''
    Inicializa o círculo com raio 0.
    '''

    self.raio = 0

  @property
  def centro(self):
    '''
    Retorna as coordenadas do centro.
    '''

    return (
      self.cx,
      self.cy
    )

  @property
  def cx(self):
    '''
    Retorna a coordenada x do centro.
    '''

    return self._cx

  @property
  def cy(self):
    '''
    Retorna a coordenada y do centro.
    '''

    return self._cy

  @property
  def limites(self):
    '''
    Retorna o quadrado delimitador do círculo.
    '''

    return (
      self.cx - self.raio,
      self.cy - self.raio,
      self.cx + self.raio,
      self.cy + self.raio
    )

  @property
  def raio(self):
    '''
    Retorna o raio do círculo.
    '''

    return self._raio

  @raio.setter
  def raio(self, valor):
    '''
    Atualiza o valor do raio.
    '''

    self._raio = valor

  def atualizar(self, x, y):
    '''
    Atualiza o raio do círculo.

    O raio é a distância do centro
    até o ponto atual do mouse.
    '''

    self.raio = (
      (x - self.cx) ** 2 +
      (y - self.cy) ** 2
    ) ** 0.5

  def incompleta(self):
    '''
    Verifica se o círculo pode ser criado.

    O círculo é considerado inválido
    se o raio for igual a 0.
    '''

    return self.raio == 0
  
  def mover(self, d_x, d_y):
    self._cx += d_x
    self._cy += d_y

  def contorno_selecao(self, x, y):
    
    distancia = ((x-self.cx)**2 + (y-self.cy)**2)**0.5
    return distancia <= self.raio
    
  def contem_ponto(self, x, y):
    
    distancia = math.sqrt((x - self.cx) ** 2 + (y - self.cy) ** 2)# o resultado é a raiz do que tá entre parenteses
    return distancia <= self.raio
