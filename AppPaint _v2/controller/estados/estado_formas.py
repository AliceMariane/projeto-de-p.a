from controller.estado import Estado

class EstadoFormas(Estado):
    
    ''' serve para qualquer figura'''
    def clicar(self, controlador, x, y):
        controlador.iniciar_fig(x, y)

    def arrastar(self, controlador, x, y):
        controlador.update_fig(x, y)

    def soltar(self, controlador):
        controlador.incluir_newfig()
