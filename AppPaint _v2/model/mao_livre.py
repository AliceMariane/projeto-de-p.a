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
