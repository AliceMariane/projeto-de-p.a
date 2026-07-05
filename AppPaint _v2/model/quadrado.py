from AppPaint_v2.model.figura import Figura

class Quadrado(Figura):
  '''
  Representa um quadrado desenhado pelo usuário.

  O quadrado é criado a partir de dois pontos:
  
  O primeiro vértice é definido quando o usuário
  pressiona o botão do mouse.

  O segundo vértice acompanha o movimento do
  mouse enquanto o botão estiver pressionado.
  '''
  
  def __init__(self, x, y, cor_borda= 'black', cor_preenchimento= ''):
    super().__init__(cor_borda, cor_preenchimento)
    '''
    Cria um novo quadrado.

    Inicialmente os dois vértices possuem
    as mesmas coordenadas.
    '''
    # Primeiro Vértice (x, y)
    self.ini_x = x
    self.ini_y = y
    
    # Segundo Vértice (x, y)
    self.fim_x = x
    self.fim_y = y

  def atualizar(self, x, y):
    '''
    Atualiza o segundo vértice (x, y) do quadrado,
    ajustando a largura e a altura para manter os lados iguais
    '''
    
    dx = x - self.ini_x
    dy = y - self.ini_y
    
    lado = max(abs(dx), abs(dy))
    self.fim_x = self.ini_x + (lado if dx >= 0 else -lado)
    self.fim_y = self.ini_y + (lado if dy >= 0 else -lado)

  def desenhar(self, canvas):
    '''
    Desenha de forma definitiva o quadrado na tela
    '''
    
    canvas.create_rectangle(self.ini_x, 
                            self.ini_y, 
                            self.fim_x, 
                            self.fim_y, 
                            outline= self.cor_borda, 
                            fill= self.cor_preenchimento)

  def desenhar_preview(self, canvas):
    '''
    Mostra o tracejado do quadrado em tempo
    real enquanto o botão do mouse está sendo pressionado
    '''
    
    canvas.create_rectangle(self.ini_x, 
                            self.ini_y, 
                            self.fim_x, 
                            self.fim_y, 
                            outline= self.cor_borda, 
                            fill= self.cor_preenchimento,
                            dash= (4, 2))

  def incompleta(self):
    '''
    Verifica se o quadrado foi desenhado corretamente.
    '''
    
    return not self.figura_valida()

  def figura_valida(self, minimo=5):
    #quadrado nao pode ser uma reta
    lado= max(
        abs(self.fim_x - self.ini_x),
        abs(self.fim_y - self.ini_y)
    )
    return lado>= minimo
