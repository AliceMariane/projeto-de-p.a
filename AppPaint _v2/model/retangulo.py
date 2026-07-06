from dataclasses import dataclass, field
from figura import Figura

@dataclass
class Retangulo(Figura):
  '''
  Representa um Retângulo.

  O retângulo é definido por dois vértices distintos.
  
  O primeiro vértice é definido quando o usuário
  pressiona o botão do mouse.

  O segundo vértice acompanha o movimento do
  mouse enquanto o botão estiver pressionado.
  '''
    
  # Primeiro Vértice (x, y)
  _ini_x : int
  _ini_y : int
  
  # Segundo Vértice (x, y)
  _fim_x : int = field(init= False)
  _fim_y : int = field(init= False)
  
  def __post_init__(self):
    '''
    Começa o segundo ponto do retangulo 
    com as mesmas coordenadas do primeiro
    '''
    
    self._fim_x = self._ini_x
    self._fim_y = self._ini_y

  @property
  def pontos(self):
    '''
    Retorna os vértices do retângulo.
    '''
    
    return (
      self._ini_x,
      self._ini_y,
      self._fim_x,
      self._fim_y
    )
    
  def atualizar(self, x, y):
    '''
    Atualiza o ultimo vértice (x, y) do retângulo
    '''
    
    self._fim_x = x
    self._fim_y = y

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva o retângulo na tela
    '''
    
    canvas.create_rectangle(*self.pontos, 
                            outline= self._cor_borda, 
                            fill= self._cor_preenchimento)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado do retângulo em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_rectangle(*self.pontos,
                            outline= self._cor_borda, 
                            fill= self._cor_preenchimento,
                            dash= (4, 2))

  def incompleta(self):
    '''
    Verifica se retangulo pode ser criado
    '''
    
    return not self._figura_valida()

  def _figura_valida (self, minimo=5):
    ''' 
    Evita fazer o retangulo se comportar como reta
    '''
    largura = abs(self._fim_x- self._ini_x)
    altura = abs(self._fim_y- self._ini_y)

    return largura>=minimo and altura>= minimo
