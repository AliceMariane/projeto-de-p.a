from dataclasses import dataclass, field
from .figura import Figura

@dataclass
class MaoLivre(Figura):
  '''
  Representa um desenho à mão livre.

  Diferentemente das demais figuras,
  o desenho livre é formado por uma sequência
  de pontos atualizados em tempo real
  durante o movimento do mouse.

  Esses pontos são ligados
  formando uma única linha.
  '''
  
  _ini_x : int
  _ini_y : int
  
  _pontos: list[tuple[int, int]] = field(init= False)
  
  def __post_init__(self):
    self._pontos = [(self._ini_x, self._ini_y)]

  @property
  def pontos(self):
    '''
    Retorna a lista de pontos do rabisco.
    '''
    
    return self._pontos
    
  def atualizar(self, x, y):
    '''
    Adiciona um novo ponto (x, y) ao rabisco
    '''
    
    self._pontos.append((x, y))

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva o rabisco na tela
    '''
    
    canvas.create_line(self.pontos, 
                        fill= self._cor_borda)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado do rabisco em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_line(self.pontos, 
                        fill= self._cor_borda,
                        dash= (4, 2))

  def incompleta(self):
    '''
    Verifica se existe pontos suficientes
    para ser considerado uma figura válida
    '''
    
    return len(self._pontos) <= 1
