from controller.estado import Estado

class EstadoSelecionar(Estado):
    
    """
    define o comportamento de selecionar
    as figuras (para, por exemplo:arrastar, copiar,         sobrepor)
    
    """
    def __init__(self, desenho):
        self.desenho = desenho
        self.figura_selecionada = None
        self.last_x = 0
        self.last_y = 0
        
       
    def clicar (self, x, y):
        self.figura_selecionada= self.desenho.buscar_figura(x,y)
        
        self.ultimo_x = x
        self.ultimo_y = y   
                       # buscar_figura é uma funcao que  
                       # sera criada na classe
                       # desenho que esta no model 
                       # pra poder apagar, copiar, mudar
                       # a figura clicada
  
    def arrastar (self, x, y):
        if self.figura_selecionada: #se a figura estiver sendo arrastada 
        
            dx = x - self.last_x
            dy = y - self.last_y
            #dx, dy ----> quanto que a figura foi movida
            #desde a ultima posicao dela
            
            self.figura_selecionada.mover(dx, dy)
             
            self.last_x = x
            self.last_y = y
       
                        
    def soltar (self, x, y):
        pass
      
