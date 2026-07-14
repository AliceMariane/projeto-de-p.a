from controller.estado import Estado


class EstadoCirculo (Estado):
    ''' 
    define o comportamento do circulo durante
    a interação do usuario com o canvas          
    '''
    def clicar (self, controlador_principal,event):
        controlador_principal.iniciar_fig(event.x, event.y)
    
    
    def arrastar (self, controlador_principal, event):
        controlador_principal.update_fig(event.x, event.y)
    
    
    def soltar (self, controlador_principal):
        controlador_principal.incluir_newfig()
