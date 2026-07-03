from Figuras.figura import Figura
from abc import dataclasses
from dataclasses import dataclass

@dataclass
class Elipse(Figura):
  ini_x : int
  ini_y : int
  fim_x : int
  fim_y : int

  def atualizar(self, x, y):
    '''
    Atualiza o segudo vértice do retângulo delimitador (x, y) da elipse
    '''
    
    self.fim_x = x
    self.fim_y = y

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva a elipse na tela
    '''
    
    canvas.create_oval(self.ini_x, 
                      self.ini_y, 
                      self.fim_x, 
                      self.fim_y, 
                      outline= self.cor_borda, 
                      fill= self.cor_preenchimento)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado da elipse em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_oval(self.ini_x, 
                      self.ini_y, 
                      self.fim_x, 
                      self.fim_y, 
                      outline= self.cor_borda, 
                      fill= self.cor_preenchimento,
                      dash= (4, 2))

  def incompleta(self):
    
    return (
    self.ini_x == self.fim_x and
    self.ini_y == self.fim_y
    )
