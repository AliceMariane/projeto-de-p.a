from AppPaint_v2.model.figura import Figura

class Reta(Figura):
  '''
  Representa uma reta desenhada pelo usuário.

  A reta é definida por dois pontos:
    > ponto inicial (ini_x, ini_y)
    > ponto final (fim_x, fim_y)

  Enquanto o botão do mouse permanece pressionado,
  o ponto final é atualizado para acompanhar o cursor.
  '''

  def __init__(self, x, y, cor_borda= 'black', cor_preenchimento= ''):
    super().__init__(cor_borda, cor_preenchimento)
    '''
    Cria uma nova reta
    
    O primeiro click do mouse define o ponto inicial,
    o ponto final começa igual ao ponto inicial.
    '''
    
    #coordenadas do ponto inicial
    self.ini_x = x
    self.ini_y = y
    
    #coordenadas do ponto final
    self.fim_x = x
    self.fim_y = y

  def atualizar(self, x, y):
    '''
    Atualiza o ultimo ponto (x, y) da reta.
    '''
    
    self.fim_x = x
    self.fim_y = y

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva a reta na tela.
    '''
    
    canvas.create_line(self.ini_x, 
                        self.ini_y, 
                        self.fim_x, 
                        self.fim_y, 
                        outline= self.cor_borda, 
                        fill= self.cor_preenchimento)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado da reta em tempo
    real enquanto o botão do mouse está sendo pressionado.
    '''
    
    canvas.create_line(self.ini_x, 
                      self.ini_y, 
                      self.fim_x, 
                      self.fim_y, 
                      outline= self.cor_borda, 
                      fill= self.cor_preenchimento,
                      dash= (4, 2))

  def incompleta(self):
      '''
      Verifica se a Reta é válida.
      
      Uma reta é considerada incompleta 
      quando os pontos são iguais.
      '''
      
      return (
      self.ini_x == self.fim_x and
      self.ini_y == self.fim_y
      )
