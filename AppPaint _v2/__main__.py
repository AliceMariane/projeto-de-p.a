from viewer.janela import Janela
from controller.controlador_principal import ControladorPrincipal

if __name__ == "__main__":
    app = Janela()

    controller = ControladorPricipal(_janela=app)

    app.notificar_controler = controller.notificar

    app.root.mainloop()
