from tkinter import * 
from tkinter import ttk
from tkinter import colorchooser
from AppPaint_v2.controller.criar_figuras import Reta, Circulo, Elipse, MaoLivre, Retangulo, Quadrado
from AppPaint_v2.controler.controlador_principal import incluir_newfig

class Janela():
  
  def __init__(self):

    self.root = Tk()
    self.root.title("Paint CAR")
    self.root.geometry("720x1080")

    paddings = {'padx': 5, 'pady': 5} 
    
    # Frame do menu
    self.f_main = Frame(self.root,
                        bg="gray",
                        padx=20,
                        relief = RAISED
                        bd=2)
    self.f_main.pack(side=LEFT, fill=Y)

    self.figuras = ['Reta', 'Circulo', 'Elipse', 'MaoLIvre', 'Retangulo', 'Quadrado']

    self.f_figuras= Frame(self.f_main,
                          bg="lightgray")
    self.f_figuras.pack(pady=10)

    for i, fig in enumerate(self.figuras):

      btao_fig = Button(self.f_figuras,
                        text = figura,
                        command=lambda f = forma: incluir_newfig(f)
      )
    btao_fig.grid(row=i, column=0, **paddings)

    # paleta de cores
    self.btao_cor = Button(self.f_main, 
                          text='Escolher Cor',
                          bg='lightgray',
                          command=self.selct_cor
    )
    
    def selct_cor(self):
        self.cor = colorchooser.askcolor(title="Escolha uma cor")[1]
        if self.cor:
            print(f'Cor escolhida: {self.cor}')

            self.btao_cor.config(bg=self.cor)
        


  def desenhar_fig(self):
    pass
    
  def limpar_tela(self):
    pass
