from AppPaint.Figuras.figura import Figura

class Quadrado(Figura):

  def __init__(self, x, y, cor_borda= 'black', cor_preenchimento= ''):
    super().__init__(cor_borda, cor_preenchimento)
    self.ini_x = x
    self.ini_y = y
    self.fim_x = x
    self.fim_y = y

    def atualizar(self, x, y):
      """
      Atualiza o ultimo ponto (x, y) do quadrado
      """
      
      self.fim_x = x
      self.fim_y = y

    def desenhar(self, canvas):
      """
      Desenha de forma definitiva o quadrado na tela
      """
      
      canvas.create_rectangle(self.ini_x, 
                              self.ini_y, 
                              self.fim_x, 
                              self.fim_y, 
                              outline= self.cor_borda, 
                              fill= self.cor_preenchimento)

    def desenhar_preview(self, canvas):
      """
      Mostra o tracejado do quadrado em tempo
      real enquanto o botão do mouse está sendo pressionado
      """
      
      canvas.create_rectangle(self.ini_x, 
                              self.ini_y, 
                              self.fim_x, 
                              self.fim_y, 
                              outline= self.cor_borda, 
                              fill= self.cor_preenchimento,
                              dash= (4, 2))

    def incompleta(self):
      '''
      Verifica se os 4 lados são iguais
      '''
      
      return (
        (self.fim_x - self.ini_x) ==
        (self.fim_y - self.ini_y)
      )
