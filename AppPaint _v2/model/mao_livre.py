from AppPaint_v2.model.figura import Figura

class MaoLivre(Figura):
  '''
  Representa um desenho à mão livre.

  Diferentemente das demais figuras,
  o desenho livre é formado por uma sequência
  de pontos atualizados em tempo real
  durante o movimento do mouse.

  Esses pontos são ligados
  formando uma única linha.
  '''
  
  def __init__(self, x, y, cor_borda= 'black'): # maolivre == rabisco
    super().__init__(cor_borda)
    
    '''
    Cria um novo desenho livremente.

    O primeiro clique do mouse gera
    o primeiro ponto da lista.
    '''
    
    self.pontos = [
      (x, y)
    ]

  def atualizar(self, x, y):
    '''
    Atualiza o ultimo ponto (x, y) do rabisco
    '''
    
    self.pontos.append((x, y))

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva o rabisco na tela
    '''
    
    canvas.create_line((self.pontos), 
                        outline= self.cor_borda)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado do rabisco em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_line((self.pontos), 
                        outline= self.cor_borda,
                        dash= (4, 2))

  def incompleta(self):
      '''
      Verifica se existe mais de 1 ponto para criar um rabisco
      '''
      
      return len(self.pontos) <= 1
