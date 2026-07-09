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
  _ini_x : int
  _ini_y : int
  
  # Segundo Vértice do retângulo delimitador (x, y)
  _fim_x : int = field(init= False)
  _fim_y : int = field(init= False)
  
  def __post_init__(self):
    '''
    Começa o segundo ponto do retangulo delimitador
    com as mesmas coordenadas do primeiro
    '''
    
    self._fim_x = self._ini_x
    self._fim_y = self._ini_y

  @property
  def pontos(self):
    '''
    Retorna os vértices do retângulo delimitador.
    '''
    
    return (
      self._ini_x,
      self._ini_y,
      self._fim_x,
      self._fim_y
    )
  
  def atualizar(self, x, y):
    '''
    Atualiza o segundo vértice do retângulo delimitador (x, y) da elipse
    '''
    
    self._fim_x = x
    self._fim_y = y

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva a elipse na tela
    '''
    
    canvas.create_oval(*self.pontos, 
                      outline= self._cor_borda, 
                      fill= self._cor_preenchimento)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado da elipse em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_oval(*self.pontos, 
                      outline= self._cor_borda, 
                      fill= self._cor_preenchimento,
                      dash= (4, 2))

  def incompleta(self):
    '''
    Verifica se a elipse pode ser criada
    
    A elipse é inválida quando 
    os dois vértices são iguais.
    '''
    
    return not self._figura_valida()

  def _figura_valida(self, minimo=5):
    ''' 
    Evita fazer o retangulo se comportar como reta
    '''
    largura = abs(self._fim_x- self._ini_x)
    altura = abs(self._fim_y- self._ini_y)

    return largura>=minimo and altura>= minimo
