from dataclasses import dataclass, field
from figura import Figura

@dataclass
class Reta(Figura):
  '''
  Representa uma reta desenhada pelo usuário.
  
  O primeiro click do mouse define o ponto inicial,
  o ponto final começa igual ao ponto inicial.
  '''

  # Primeiro Vértice (x, y)
  _ini_x : int
  _ini_y : int
  
  # Segundo Vértice (x, y)
  _fim_x : int = field(init= False)
  _fim_y : int = field(init= False)
  
  @property
  def pontos(self):
    '''
    Retorna os vértices da reta.
    '''
    
    return (
      self._ini_x,
      self._ini_y,
      self._fim_x,
      self._fim_y
    )
    
  def __post_init__(self):
    '''
    Inicializa o ponto final da reta
    com as mesmas coordenadas do ponto inicial
    '''
    
    self._fim_x = self._ini_x
    self._fim_y = self._ini_y

  def atualizar(self, x, y):
    '''
    Atualiza o ultimo ponto (x, y) da reta.
    '''
    
    self._fim_x = x
    self._fim_y = y

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva a reta na tela.
    '''
    
    canvas.create_line(*self.pontos, 
                        fill= self._cor_borda)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado da reta em tempo
    real enquanto o botão do mouse está sendo pressionado.
    '''
    
    canvas.create_line(*self.pontos, 
                      fill= self._cor_borda,
                      dash= (4, 2))

  def incompleta(self):
    '''
    Verifica se a Reta é válida.
    
    Uma reta é considerada incompleta 
    quando os pontos são iguais.
    '''
    
    return (
    self._ini_x == self._fim_x and
    self._ini_y == self._fim_y
    )
    
