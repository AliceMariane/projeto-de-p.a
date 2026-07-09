from tkinter import *
from tkinter import ttk
from viewer.janela import Janela
from controller.controlador_principal import ControladorPrincipal




def main():
    controller = ControladorPrincipal()
    view = Janela(controller.notificar)
    controller._janela = view
    view.root.mainloop()

if __name__ == "__main__":
    main()
