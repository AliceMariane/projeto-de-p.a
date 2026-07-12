from .estado import Estado


class EstadoReta (Estado):
    ''' 
    define o comportamento da linha durante
    a interação do usuario com o canvas          
    '''
    def clicar (self, controlador_principal,event):
        controlador_principal._model.iniciar_fig(event.x, event.y)
    
    
    def arrastar (self, controlador_principal, event):
        controlador_principal._model.update_fig(event.x, event.y)
    
    
    def soltar (self, controlador_principal, event):
        controlador_principal._model.incluir_newfig()