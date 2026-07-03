from tkinter import * 
from tkinter import colorchooser
import sys
import os

# Comando Principal

# Janela principal
class Janela:

    def __init__(self, root):

        self.root = root
        self.root.title('Paint CAR')
        self.root.geometry('720x1080')

        self.cor_atual = 'black'
        self.icone()
        self.menu()
        self.area_d()

    def icone (self):
        icon = os.path.dirname(os.path.abspath(__file__))
        # aplicando o icone em quaisquer OS
        try:
            if sys.platform.startswith('win'):
                caminho = os.path.join(icon,'icone_pa.ico')
                if os.path.exists(caminho):
                    self.root.iconbitmap(caminho)
            else:
                caminho = os.path.join(icon, 'icone_pa.png')
                img = PhotoImage(file=caminho)
                self.root.iconphoto(True, img)

        except Exception as e:
            print(f'Icone invalido: {e}')

        # Menu principal
    
    def menu (self):

        self.frame_menu = Frame(self.root, bg='gray', pady=20, relief=RAISED, bd=2)
        self.frame_menu.pack(fill=X)

        # outros frames incluidos no menu principal

        self.f_cores = Frame(self.frame_menu, bg='lightgray', relief=RAISED, bd=2)
        self.f_cores.pack(side=LEFT, padx=10)

        self.f_figuras = Frame(self.frame_menu, bg='lightgray', relief=RAISED, bd=2)
        self.f_figuras.pack(side=LEFT, padx=10)

        self.f_pincel = Frame(self.frame_menu,bg ='lightgray', relief=RAISED, bd=2)
        self.f_pincel.pack(side=LEFT, padx=10)

        
        

        self.btao_c() # paleta de cores

        btao_paleta = Button(self.f_cores, text='Paleta', command=self.palet_c)
        btao_paleta.grid(row=0,column=10, padx=5)

        self.figuras()
        self.pincels()


    def define_cores(self, nova_cor):

        self.cor_atual = nova_cor
        print(f'Cor atual: {self.cor_atual}')

    def btao_c(self):

        lst_cores = ['red', 'green', 'blue','yellow', 'orange',
                'brown', 'pink', 'black', 'white']

        for i, cor_ in  enumerate(lst_cores):
            btao = Button(
                self.f_cores,
                bg=cor_,
                width=2,
                height=1,
                command=lambda c=cor_:self.define_cores(c)
                
            )
            btao.grid(row=0, column=i, padx=2)
        
    def palet_c(self):
            
        cor = colorchooser.askcolor(title='Escolha uma cor')[1]
            
        if cor:
            self.define_cores(cor)
            print(f'Cor escolhida: {cor}')
                
    def figuras(self):

        figuras_lst = ['Circulo', 'Quadrado', 'Retangulo', 'Oval']

        for i, figura in enumerate(figuras_lst):
            btao_figura = Button(
                self.f_figuras,
                text=figura,
                command = lambda f=figura: print(f'{f} selecionado')
            )

            btao_figura.grid(row=0, column=i, padx=5)
    def pincels (self):

        pincel_lst = ["Reta", "Curvo", "Tracejado", "Borracha"]
        
        for i, pincel in enumerate(pincel_lst):
            
            btao_pincel = Button(
                self.f_pincel,
                text=pincel,
                command=lambda  p=pincel: print(f'{p} selecionado')
            )
            btao_pincel.grid(row=0, column=i,padx=5)
            
    def area_d(self):
        
        self.canvas = Canva(self.root, bg='white')
        self.canvas.pack(fill=BOTH, expand=True)
            
