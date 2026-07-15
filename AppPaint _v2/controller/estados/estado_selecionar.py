from controller.estado import Estado


class EstadoSelecionar(Estado):
    '''
    Estado responsável pela seleção e movimentação das figuras.

    Este estado apenas encaminha os eventos do mouse para o
    ControladorPrincipal, que possui toda a lógica da aplicação.
    '''

    def clicar(self, controlador, x, y):
        '''
        Solicita ao controlador que selecione uma figura.
        '''
        controlador.selecionar_figura(x, y)

    def arrastar(self, controlador, x, y):
        '''
        Solicita ao controlador mover a figura selecionada.
        '''
        controlador.mover_figura(x, y)

    def soltar(self, controlador):
        '''
        Finaliza o movimento.
        '''
        controlador.finalizar_movimento()
