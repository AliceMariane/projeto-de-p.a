from tkinter import *
from tkinter import ttk
from tkinter import colorchooser, filedialog

from utils.cores import Cores
from controller.criar_renderizadores import CriarRenderizadores

# import os
# from PIL import Image, ImageTk


def incluir_newfig(formas):
  print(f"->Ok:'{formas}'")


class Janela:

  def __init__(self, controller_callback=None):
    self.root = Tk()
    self.root.title("𓂃Paint𓂃🖌")
    self.root.geometry("720x1080")

    # Controle de erros
    self.notificar_controller = (
      controller_callback
      if controller_callback
      else self.mock_controller
    )

    self.cor_borda = 'black'  # c = cor
    self.cor_preenchimento = 'white'
    self.icones_em_memoria = {}

    # Referência para as cores do controlador
    self._cores: Cores | None = None

    # Construir layout
    self.layout()


  # Metodos temporarios
  def mock_controller(self, acao, valor):
    print(f'Controller acionado: {acao} -> {valor}')


  def set_cores(self, cores: Cores):
    self._cores = cores


  # funcao para rodar o codigo
  def btao_icone(self, container, text, nome_icone, command):
    return Button(
      container,
      text=text,
      command=command,
      width=10
    )


  def abrir_paleta(self, tipo):
    cor = colorchooser.askcolor()[1]

    if cor:

      self.notificar_controller('mudar_cor', (tipo, cor))

      if tipo == 'borda':
        self.btao_cor_borda.config(bg=cor)

      elif tipo == 'preenchimento':
        self.btao_cor_preenchimento.config(bg=cor)


  def layout(self):
    self.paddings = {'padx': 5, 'pady': 5}

    # Frame do menu
    self.f_menu = Frame(
      self.root,
      bg="#2b2b2b",
      width=230,
      relief=RAISED,
      bd=2
    )

    self.f_menu.pack(side=LEFT, fill=Y)
    self.f_menu.pack_propagate(False)

    # Menu canva
    self.canvas = Canvas(
      self.root,
      bg="white",
      cursor="pencil"
    )

    self.canvas.pack(
      side=RIGHT,
      fill=BOTH,
      expand=True
    )

    # eventos do mouse
    self.canvas.bind("<Button-1>", self.iniciar_desenho)
    self.canvas.bind("<B1-Motion>", self.atualizar_desenho)
    self.canvas.bind("<ButtonRelease-1>", self.finalizar_desenho)

    # Separação do f_main(Menu principal)
    self.menu_formas()
    self.menu_ferramentas()
    self.menu_cores()
    self.menu_visualizacao()


  def menu_formas(self):

    Label(
      self.f_menu,
      text='╰⌲Formas',
      bg="#2B2D31",
      fg="white",
      font=("Arial", 10, "bold")
    ).pack(pady=(20, 8))

    f_grid = Frame(
      self.f_menu,
      bg="#2B2D31"
    )

    f_grid.pack()

    formas = [
      {'id': 'reta', 'nome': 'Reta'},
      {'id': 'maolivre', 'nome': 'Mao Livre'},
      {'id': 'circulo', 'nome': 'Circulo'},
      {'id': 'retangulo', 'nome': 'Retangulo'},
      {'id': 'quadrado', 'nome': 'Quadrado'},
      {'id': 'elipse', 'nome': 'Elipse'}
    ]

    row_idx = 0
    col_idx = 0

    for forma in formas:

      btao = self.btao_icone(
        container=f_grid,
        text=forma['nome'],
        nome_icone=forma['id'],
        command=lambda f=forma['id']:
          self.notificar_controller('selecionar_forma', f)
      )

      btao.grid(
        row=row_idx,
        column=col_idx,
        padx=2,
        pady=5
      )

      col_idx += 1

      if col_idx > 1:
        col_idx = 0
        row_idx += 1


  def menu_ferramentas(self):

    Label(
      self.f_menu,
      text='╰⌲Ferramentas',
      bg='#2B2D31',
      fg='white',
      font=("Arial", 10, "bold")
    ).pack(pady=(20, 8))

    Button(
      self.f_menu,
      text='Abrir Projeto',
      bg='#3A3D41',
      fg='white',
      relief=FLAT,
      command=lambda:
        self.notificar_controller('abrir', None)
    ).pack(fill=X, padx=10, pady=4)

    Button(
      self.f_menu,
      text='Salvar Projeto',
      bg='#3A3D41',
      fg='white',
      relief=FLAT,
      command=lambda:
        self.notificar_controller('salvar', None)
    ).pack(fill=X, padx=10, pady=4)

    Button(
      self.f_menu,
      text="Borracha",
      bg="#3A3D41",
      fg='white',
      relief=FLAT,
      command=lambda:
        self.notificar_controller(
          'selecionar_ferramenta',
          'borracha'
        )
    ).pack(fill=X, padx=10, pady=4)

    Label(
      self.f_menu,
      text="Estilo do Traço:",
      bg="#2B2D31",
      fg='gray',
      font=('Arial', 8)
    ).pack(anchor=W, padx=10)

    self.cb_estilo = ttk.Combobox(
      self.f_menu,
      values=[
        "Solido",
        "Tracejado",
        "Pontilhado"
      ],
      state="readonly"
    )

    self.cb_estilo.current(0)
    self.cb_estilo.pack(fill=X, padx=10, pady=4)

    self.cb_estilo.bind(
      '<<ComboboxSelected>>',
      lambda e:
        self.notificar_controller(
          "mudar_estilo",
          self.cb_estilo.get()
        )
    )


  def caminho_salvar(self):
    caminho = filedialog.asksaveasfilename(
      defaultextension='.pkl',
      filetypes=[
        ("arq paint", "*.pkl"),
        ("Todos os arquivos", "*.*")
      ],
      title="Salvar Projeto como"
    )

    return caminho


  def caminho_abrir(self):
    caminho = filedialog.askopenfilename(
      defaultextension='.pkl',
      filetypes=[
        ('arq paint', '*.pkl'),
        ('Todos os arquivos', '*.*')
      ],
      title='Abrir Projeto'
    )

    return caminho


  def menu_cores(self):

    Label(
      self.f_menu,
      text="╰⌲CORES",
      bg="#2B2D31",
      fg='white',
      font=("Arial", 10, "bold")
    ).pack(pady=(20, 8))

    self.btao_cor_borda = Button(
      self.f_menu,
      text='Cor da borda',
      bg='black',
      fg='white',
      relief=FLAT,
      command=lambda: self.abrir_paleta("borda")
    )

    self.btao_cor_borda.pack(fill=X, padx=10, pady=4)

    self.btao_cor_preenchimento = Button(
      self.f_menu,
      text='preenchimento',
      bg='black',
      fg='white',
      relief=FLAT,
      command=lambda: self.abrir_paleta('preenchimento')
    )

    self.btao_cor_preenchimento.pack(fill=X, padx=10, pady=4)


  def menu_visualizacao(self):
    '''
    Label(
      self.f_menu,
      text='VISUALIZAÇÃO',
      bg='#69b0fc',
      fg='white',
      font=('Arial', 10, 'bold')
    ).pack(pady=(15, 5))

    f_zoom = Frame(self.f_menu, bg="#69b0fc")
    f_zoom.pack(fill=X, padx=10)

    Button(
      f_zoom,
      text="Zoom + ",
      bg="#4a4a4a",
      fg='white',
      relief=FLAT,
      width=7,
      command=lambda:
        self.notificar_controller('zoom', 'in')
    ).pack(side=LEFT, expand=True, padx=(0, 2))

    Button(
      f_zoom,
      text="Zoom - ",
      bg="#4a4a4a",
      fg='white',
      relief=FLAT,
      width=7,
      command=lambda:
        self.notificar_controller('zoom', 'out')
    ).pack(side=RIGHT, expand=True, padx=(2, 0))
    '''
    Button(
      self.f_menu,
      text="Exportar PNG",
      command=lambda:
          self.notificar_controller("exportar_png", None)
    ).pack(fill=X, padx=10, pady=2)
    
    Button(
      self.f_menu,
      text="Limpar Tela",
      bg="#8a2e2e",
      fg='white',
      relief=FLAT,
      command=lambda:
        self.notificar_controller('limpar_tela', None)
    ).pack(side=BOTTOM, fill=X, padx=10, pady=20)

 
  def iniciar_desenho(self, event):
    self.notificar_controller(
      "inicio",
      (event.x, event.y)
    )


  def atualizar_desenho(self, event):
    self.notificar_controller(
      "arrastar",
      (event.x, event.y)
    )


  def finalizar_desenho(self, event):
    self.notificar_controller("fim",None)


  def redesenhar(self, figuras_pronta, figura_atual=None):
    self.canvas.delete("all")  # limpa a tela

    if self._cores is None:
      return

    # Desenhar figuras prontas
    for figura in figuras_pronta:
      renderizador = CriarRenderizadores.criar(figura)
      renderizador.desenhar(
        self.canvas,
        figura,
        self._cores
      )

    # Desenhar preview da figura atual
    if figura_atual is not None:
      renderizador = CriarRenderizadores.criar(figura_atual)
      renderizador.desenhar_preview(
        self.canvas,
        figura_atual,
        self._cores
      )
  

  def caminho_salvar_png(self):

    return filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Imagem PNG", "*.png")]
    )

#esse codigo ta grande demais e sinto que talvez fosse melhor colocar
#algumas coisas daqui em uma nova classe, se possivel 
