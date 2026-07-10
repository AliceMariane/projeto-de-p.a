from tkinter import * 
from tkinter import ttk
from tkinter import colorchooser
from controller.criar_figuras import Reta, Circulo, Elipse, MaoLivre, Retangulo, Quadrado #se me lembrar de ter alterado outras coisas volto aqui (alice)
#from controlador_principal import incluir_newfig<---------- isso tava causando erro de importacoes circulares, cuidado!!!
#import os
#from PIL import Image, ImageTk

def incluir_newfig(formas):
   print(f"->Ok:'{formas}'")
   
   
   
class Janela():
  
    def __init__(self, controller_reechamada=None):
        self.root = Tk()
        self.root.title("Paint CAR")
        self.root.geometry("720x1080")
    # Controle de erros
        self.notificar_controller = (controller_reechamada if controller_reechamada else self.mock_controller)

        self.c_linha = 'black' # c = cor
        self.c_fundo = 'white'
        self.icones_em_memoria = {}
        # Construir layout
        self.layout()
        
# Metodos temporarios
    def mock_controller(self, acao, valor):
       print(f'Controller acionado: {acao} ->{valor}')

# funcao para rodar o codigo
    def btao_icone(self, container, text, nome_icone, command ):
       return Button(container, text=text, command=command, width=10)

    def abrir_paleta(self, tipo):
       cor = colorchooser.askcolor()[1]
       if cor:
          print (f'Cor escolhida para {tipo}: {cor}')

    def layout(self):
       self.paddings = {'padx': 5, 'pady': 5} 
    
    # Frame do menu
       self.f_menu = Frame(self.root,
                        bg="#2b2b2b",
                        width=150,
                        relief = RAISED,
                        bd=2)
       self.f_menu.pack(side=LEFT, fill=Y)
       self.f_menu.pack_propagate(False)

    # Menu canva
       self.canvas = Canvas(self.root,
                         bg="white",
                         cursor="crosshair")
       self.canvas.pack(side=RIGHT,
                            fill=BOTH,
                            expand=True)
       #eventos do mouse
       self.canvas.bind("<Button-1>", self.comecar_desenho)
       self.canvas.bind("<B1-Motion>", self.arrastar_desenho)
       self.canvas.bind("<ButtonRelease-1>", self.acabar_desenho)
       
    # Separação do f_main(Menu principal)
       self.menu_formas()
       self.menu_ferramentas()
       self.menu_cores()
       self.menu_visualizacao()

    def menu_formas(self):

       Label(self.f_menu,
             text='Formas',
             bg="#69b0fc", fg="white", font=("Arial", 10, "bold")).pack(pady=(15, 5))
       f_grid = Frame(self.f_menu,
                      bg="#69b0fc")
       f_grid.pack()

       formas = [{'id': 'reta', 'nome': 'Reta'},
            {'id': 'maolivre', 'nome':'Mao Livre'},
            {'id': 'circulo', 'nome':'Circulo'},
            {'id': 'retangulo', 'nome':'Retangulo'},
            {'id': 'quadrado', 'nome':'Quadrado'},
             {'id': 'elipse', 'nome': 'Elipse'}
               ]
       row_idx, col_idx = 0, 0 
       for forma in formas:
            btao = self.btao_icone(
            container=f_grid,
            text=forma['nome'],
            nome_icone=forma['id'],
            command=lambda f=forma['id']: self.notificar_controller('selecionar_forma', f)
        )
            btao.grid(row=row_idx, column= col_idx, padx=2, pady=2)
            col_idx += 1
       
            if col_idx > 1:
                col_idx = 0
                row_idx += 1

    def menu_ferramentas(self):
       Label(self.f_menu, text= 'Ferramentas',
             bg='#69b0fc', fg='white',
             font=("Arial", 10, "bold")).pack(pady=(15, 5))
       
       Button(self.f_menu, text="Borracha",
               bg="#4a4a4a", fg='white',   
               relief=FLAT,
               command=lambda: self.notificar_controller('selecionar_ferramenta', 'borracha')).pack(fill=X,padx=10, pady=2)
       Label(self.f_menu, text="Estilo do Traço:", bg="#69b0fc", fg='gray',
                     font=('Arial', 8)).pack(anchor=W, padx=10)
       self.cb_estilo = ttk.Combobox(self.f_menu, values=["Solido", "Tracejado", "Pontilhado"], state="readonly")
       self.cb_estilo.current(0)
       self.cb_estilo.pack(fill=X, padx=10,pady=2)

       self.cb_estilo.bind('<<ComboboxSelected>>', lambda e :self.notificar_controller("mudar_estilo", self.cb_estilo.get()))

    def menu_cores(self):
       Label(self.f_menu,
             text="CORES", bg="#69b0fc", fg='white',
             font=("Arial", 10, "bold")).pack(pady=(15, 5))
       self.btao_cor_linha = Button(self.f_menu,
                                    text='Cor da Linha',
                                     bg=self.c_linha, fg='white',
                                     relief=FLAT,
                                     command=lambda : self.abrir_paleta("linha"))
       self.btao_cor_linha.pack(fill=X, padx=10, pady=2)

       self.btao_cor_fundo = Button(self.f_menu,
                                    text='Cor do fundo',
                                    bg='white', fg='black', 
                                    relief=FLAT,
                                    command=lambda: self.abrir_paleta('fundo')
                                    )
       self.btao_cor_fundo.pack(fill=X, padx=10 ,pady=2)

    def menu_visualizacao(self):
       Label(self.f_menu,
             text='VISUALIZAÇÃO',
             bg='#69b0fc', fg='white',
             font=('Arial', 10, 'bold')).pack(pady=(15, 5))
       f_zoom = Frame(self.f_menu, bg="#69b0fc")
       f_zoom.pack(fill=X, padx=10)

       Button(f_zoom,
              text="Zoom + ",
              bg="#4a4a4a", fg='white',
              relief=FLAT,
              width=7,
              command=lambda: self.notificar_controller('zoom', 'in')).pack(side=LEFT, expand=True, padx=(0,2))
       
       Button(f_zoom,
                     text="Zoom - ",
                     bg="#4a4a4a", fg='white',
                     relief=FLAT,
                     width=7,
                     command=lambda: self.notificar_controller('zoom', 'out')).pack(side=RIGHT, expand=True,padx=(2, 0))
       
       Button(self.f_menu, 
              text="Limpar Tela",
              bg="#8a2e2e", fg='white', 
            relief=FLAT,
            command=lambda: self.notificar_controller('limpar_tela',None)).pack(side=BOTTOM, fill=X, padx=10, pady=20)
       
    def comecar_desenho(self, event):
        print("Clicaram:", event.x, event.y)
        self.notificar_controller("inicio", (event.x, event.y))


    def arrastar_desenho(self, event):
       self.notificar_controller("arrastar", (event.x, event.y))


    def acabar_desenho(self, event):
       self.notificar_controller("fim", None)
       
    def redesenhar(self, figuras_pronta, figura_atual=None):
        self.canvas.delete("all")   # limpa a tela

        #Desenhar figura selecionada
        for figura in figuras_pronta:
           figura.desenhar(self.canvas)

        if figura_atual:
           figura_atual.desenhar_preview(self.canvas)

        
    


                      
    

