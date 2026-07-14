from viewer.janela import Janela
from controller.controlador_principal import ControladorPrincipal

if __name__ == "__main__":
    app = Janela()

    controller = ControladorPrincipal(_janela=app) # era algo bobo, apenas um erro ortografico que ocorreu

    app.notificar_controller = controller.notificar
    app.set_cores(controller._cores)

    app.root.mainloop()
