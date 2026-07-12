from .estado import Estado


class EstadoMaoLivre(Estado):
    ''' 
    define o comportamento de mao livre durante
    a interação do usuario com o canvas          
    '''
    def clicar (self, controlador_principal,event):
        controlador_principal.iniciar_fig(event.x, event.y)
    
    
    def arrastar (self, controlador_principal, event):
        controlador_principal.update_fig(event.x, event.y)
    
    
    def soltar (self, controlador_principal, event):
        controlador_principal.incluir_newfig()
