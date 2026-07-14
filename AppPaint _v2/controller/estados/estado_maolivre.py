from controller.estado import Estado


class EstadoMaoLivre(Estado):
    ''' 
    define o comportamento de mao livre durante
    a interação do usuario com o canvas          
    '''
    def clicar (self, controlador, x, y):
        controlador.iniciar_fig(x, y)
    
    
    def arrastar (self, controlador, x, y):
        controlador.update_fig(x, y)
    
    
    def soltar (self, controlador):
        controlador.incluir_newfig()
