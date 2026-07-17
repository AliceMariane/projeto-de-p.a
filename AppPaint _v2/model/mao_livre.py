from dataclasses import dataclass, field
from .figura import Figura


@dataclass
class MaoLivre(Figura):
  '''
  Representa um rabisco desenhado pelo usuário.

  A figura é composta por uma sequência
  de pontos percorridos pelo mouse.
  '''
  _ini_x: int
  _ini_y: int

  cor_borda: str ='black'
  cor_preenchimento: str='white'

  _pontos: list = field(init=False)
  
  def __post_init__(self):
    self._pontos = [self._ini_x, self._ini_y, self._ini_x, self._ini_y]
    

  
  @property
  def pontos(self):
    '''
    Retorna a lista de pontos do rabisco.
    '''

    return self._pontos

  @pontos.setter
  def pontos(self):
    '''
    Atualiza a lista de pontos do rabisco.
    '''

    return self._pontos

  def atualizar(self, x, y):
    '''
    Adiciona um novo ponto ao rabisco.
    '''

    self.pontos.extend([x,y])


  def incompleta(self):
    '''
    Verifica se o rabisco é válido.

    Um rabisco é considerado incompleto
    quando possui menos de dois pontos.
    '''

    return len(self.pontos) < 2

  def mover(self, d_x, d_y):

    for i in range(0, len(sekf.pontos), 2):
      self.pontos[i] += d_x
      self.pontos[i+1] += d_y

  def contorno_selecao(self, x, y):

    for i in range(0, len(self.pontos), 2):
      px = self.pontos[i]
      py = self.pontos[i+1]
      distancia = ((x - px)**2 + (y - py)**2)**0.5
      if distancia <= 5:
        return True
    return False

  def contem_ponto(self, x, y, tolerancia=5):
    '''
    Verifica se o ponto (x, y) está próximo
    de algum segmento do rabisco.
    '''

    pontos = self.pontos

    for i in range(0, len(pontos) - 2, 2):
      x1, y1 = pontos[i], pontos[i + 1]
      x2, y2 = pontos[i + 2], pontos[i + 3]

      px = x2 - x1
      py = y2 - y1
      
      somados_quadrados = px ** 2 + py ** 2
      
      if somados_quadrados == 0:
        distancia = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
        if distancia <= tolerancia:
          return True
        continue

      u = ((x - x1) * px + (y - y1) * py) / float(somados_quadrados)
      u = max(0, min(1, u))

      x_proximo = x1 + u * px
      y_proximo = y1 + u * py

      distancia = ((x - x_proximo) ** 2 + (y - y_proximo) ** 2) ** 0.5
      if distancia <= tolerancia:
        return True
