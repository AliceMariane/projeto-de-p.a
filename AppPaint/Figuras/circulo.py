from AppPaint.Figuras.figura import Figura

class Circulo(Figura):

  def __init__(self, x, y, cor_borda= "black", cor_preenchimento= ''):
    super().__init__(cor_borda, cor_preenchimento)
    self.cx = x
    self.cy = y
    self.raio = 0
    
  def atualizar(self, x, y):
    '''
    Atualiza o tamanho do raio
    '''
    
    self.raio = ((self.cx)**2 +
                 (self.cy)**2 
                ) **0.5
  
  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva o cículo na tela
    '''
    
    canvas.create_oval(self.cx - self.raio,
                      self.cy - self.raio, 
                      self.cx + self.raio, 
                      self.cy + self.raio,
                      outline= self.cor_borda, 
                      fill= self.cor_preenchimento)
  
  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado do círculo em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_oval(self.cx - self.raio,
                      self.cy - self.raio, 
                      self.cx + self.raio, 
                      self.cy + self.raio,
                      outline= self.cor_borda, 
                      fill= self.cor_preenchimento,
                      dash= (4, 2))
  
  def incompleta(self):
    '''
    Só vira círculo se o raio for maior q 0
    '''
    
    return self.raio == 0
