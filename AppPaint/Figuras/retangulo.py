from AppPaint.Figuras.figura import Figura

class Retangulo(Figura):
  '''
  Representa um Retângulo.

  O retângulo é definido por dois vértices distintos.
  
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
    """
    Atualiza o ultimo vértice (x, y) do retângulo
    """
    
    self.fim_x = x
    self.fim_y = y

  def desenhar(self, canvas):
    """
    Desenha de forma definitiva o retângulo na tela
    """
    
    canvas.create_rectangle(self.ini_x, 
                            self.ini_y, 
                            self.fim_x, 
                            self.fim_y, 
                            outline= self.cor_borda, 
                            fill= self.cor_preenchimento)

  def desenhar_preview(self, canvas):
    """
    Mostra o tracejado do retângulo em tempo
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
    Verifica se o Retângulo é válido.

    A elipse é inválida quando 
    os dois vértices são iguais.
    '''
      
    return (
    self.ini_x == self.fim_x and
    self.ini_y == self.fim_y
    )
