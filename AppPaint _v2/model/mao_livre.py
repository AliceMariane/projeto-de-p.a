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
