from dataclasses import dataclass, field
from .figura import Figura

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

  _raio: float = field(init=False)
  
  def __post_init__(self):
    '''  
    Inicializa o circulo com raio 0
    '''
    
    self._raio = 0
  
  @property
  def centro(self):
    '''
    Retorna as coordenadas do centro
    '''
    
    return (self.cx, self.cy)
  
  @property
  def cx(self):
    return self._cx
  
  @property
  def cy(self):
    return self._cy
  
  @property
  def limites(self):
    '''
    Retorna o quadrado delimitador do círculo
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
    Retorna o raio do circulo
    '''
    
    return self._raio
  
  @raio.setter
  def raio(self, valor):
    '''
    Atualiza o valor do raio
    '''
    
    self._raio = valor
    
  def atualizar(self, x, y):
    '''
    Atualiza o raio do Círculo
    
    O raio é a distância do centro
    até o ponto atual do mouse
    '''
    
    self.raio = ((x - self.cx)**2 +
                 (y- self.cy)**2 
                ) **0.5
  
  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva o cículo na tela
    '''
    
    canvas.create_oval(*self.limites,
                      outline= self._cor_borda, 
                      fill= self._cor_preenchimento)
  
  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado do círculo em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_oval(*self.limites,
                      outline= self._cor_borda, 
                      fill= self._cor_preenchimento,
                      dash= (4, 2))
  
  def incompleta(self):
    '''
    Verifica se o círculo pode ser criado.
    
    O círculo é considerado inválido
    se o raio for igual a 0
    '''
    
    return self.raio == 0
