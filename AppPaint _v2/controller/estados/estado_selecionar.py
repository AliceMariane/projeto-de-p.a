from controller.estado import Estado
from dataclasses import dataclass

@dataclass
class EstadoSelecionar(Estado):
    
    """
    define o comportamento de selecionar
    as figuras (para, por exemplo:arrastar, copiar,         sobrepor)
    
    """
    
    #desenho: desenho = desenho
    figura_selecionada = None
    
    last_x: int = 0
    last_y: int = 0
       
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
      
    def copiar(self):
        self.controlador.clipboard = self.figura_selecionada.clone() # clipboard== area de transferencia
        
    def colar(self):
        
        nova_copia = self.controlador.clipboard.clone()
        self.controlador.model.adicionar(nova_copia)
        
    def trazer_para_frente(self):
        self.controlador.model.trazer_para_frente (self.figura_selecionada)
        
    def jogar_para_tras(self):
        self.controlador.model.jogar_para_tras (self.figura_selecionada)
        
    def apagar (self):
        ...
