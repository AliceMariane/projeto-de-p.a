from dataclasses import dataclass, field
from .figura import Figura


@dataclass
class MaoLivre(Figura):
  '''
  Representa um rabisco desenhado pelo usuário.

  A figura é composta por uma sequência
  de pontos percorridos pelo mouse.
  '''

  _pontos: list = field(default_factory=list)

  @property
  def pontos(self):
    '''
    Retorna a lista de pontos do rabisco.
    '''

    return self._pontos

  @pontos.setter
  def pontos(self, valor):
    '''
    Atualiza a lista de pontos do rabisco.
    '''

    self._pontos = valor

  def atualizar(self, x, y):
    '''
    Adiciona um novo ponto ao rabisco.
    '''

    self.pontos.append((x,y))


  def incompleta(self):
    '''
    Verifica se o rabisco é válido.

    Um rabisco é considerado incompleto
    quando possui menos de dois pontos.
    '''

    return len(self.pontos) < 2
