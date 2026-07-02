from AppPaint.Figuras.figura import Figura

class Circulo(Figura):
  '''
  Representa um círculo desenhado pelo usuário.

  O círculo é definido por:
    > centro (cx, cy)
    > raio

  O centro é definido no primeiro clique do mouse.

  Enquanto o usuário arrasta o mouse,
  o raio é recalculadoem tempo real utilizando
  a distância entre o centro e a posição atual do mouse.
  '''
  
  def __init__(self, x, y, cor_borda= "black", cor_preenchimento= ''):
    super().__init__(cor_borda, cor_preenchimento)
    '''
    Cria um novo círculo.

    O primeiro clique define o centro do círculo.

    Inicialmente o raio vale zero,
    sendo atualizado durante o movimento do mouse.
    '''
    
    # Coordenadas do Centro
    self.cx = x
    self.cy = y
    
    # Raio Inicial
    self.raio = 0
    
  def atualizar(self, x, y):
    '''
    Atualiza o raio do Círculo
    
    O raio é a distância do centro
    até o ponto atual do mouse
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
    Verifica se o círculo pode ser criado.
    
    O círculo é considerado inválido
    se o raio for igual a 0
    '''
    
    return self.raio == 0
