from AppPaint_v2.model.figura import Figura

class Elipse(Figura):
  '''
  Representa uma elipse.

  A elipse é construída a partir do retângulo
  delimitador formado por dois vértices opostos.

  Esses vértices são definidos pelo clique
  inicial e pela posição atual do mouse.
  '''
  
  def __init__(self, x, y, cor_borda= 'black', cor_preenchimento= ''):
    super().__init__(cor_borda, cor_preenchimento)
    
    # Primeiro Vértice do retângulo delimitador (x, y)
    self.ini_x = x
    self.ini_y = y
    
    # Segundo Vértice do retângulo delimitador (x, y)
    self.fim_x = x
    self.fim_y = y

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
    '''
    Verifica se a elipse pode ser criada
    
    A elipse é inválida quando 
    os dois vértices são iguais.
    '''
    
    return (
    self.ini_x == self.fim_x and
    self.ini_y == self.fim_y
    )
