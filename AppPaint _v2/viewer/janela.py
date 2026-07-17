from tkinter import *
from tkinter import ttk
from tkinter import colorchooser, filedialog
from tkinter import messagebox

from utils.cores import Cores
from controller.criar_renderizadores import CriarRenderizadores

# import osfrom tkinter import messagebox
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
    self.barra_menu()
    self.layout()
    
  def sobre_projeto (self):
    messagebox.showinfo(
        "Sobre",
        "paint v2\n\n"
        "feito por: Rai Santos, Alice Mariane, Caique Souza.\n\n "
        "Projeto desenvolvido como atividade acadêmica.\n\n"
        "Curso de Ciência da Computação\n"
        "Universidade Federal de Sergipe - UFS\n\n"
        "Aplicação de desenho desenvolvida em Python com Tkinter.\n\n"
        "Utiliza arquitetura MVC e State Pattern.\n"
        
    )

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
    
     # atalhos de teclado
    self.root.bind_all(
        "<Control-c>",
        lambda event: self.notificar_controller("copiar", None))

    self.root.bind_all(
        "<Control-v>",
        lambda event: self.notificar_controller("colar", None))

    self.root.bind_all(
        "<Up>",
        lambda event: self.notificar_controller("frente", None))
    
    self.root.bind_all(
        "<Down>",
        lambda event: self.notificar_controller("tras", None))
    
    self.root.bind_all(
        "<Delete>",
        lambda event: self.notificar_controller("apagar", None))

    self.root.bind(
        "<Right>",
        lambda e: self.notificar_controller('direita', None))
    
    self.root.bind(
        "<Left>",
        lambda e: self.notificar_controller('esquerda', None))
    
    # eventos de menu do botao direito do mouse
    self.canvas.bind("<Button-3>", self.menu_contexto)
    
    # Separação do f_main(Menu principal)
    self.menu_formas()
    self.menu_ferramentas()
    self.menu_cores()
    self.menu_visualizacao()
    self.menu_camadas()

  
  def menu_formas(self):

    '''Label(
      self.f_menu,
      text='╰⌲Formas',
      bg="#2B2D31",
      fg="white",
      font=("Arial", 10, "bold")
    ).pack(pady=(20, 8))'''

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
          self.clicar_forma(f)
      )

      col_idx += 1

      if col_idx > 1:
        col_idx = 0
        row_idx += 1

  def clicar_forma(self, forma):

    self.forma_atual = forma
    if getattr(self, 'modo_selecao', False):
      self.alterar_selecao()

    self.notificar_controller('selecionar_forma', forma)

  def alterar_selecao(self):

    self.modo_selecao = not getattr(self, 'modo_selecao', False)
    if self.modo_selecao:
      self.btao_selecionar.config(
        text='↖ SELEÇÃO: ON',
        bg='#4CAF50',
        fg='white',
        relief=SUNKEN
      )
      self.notificar_controller('selecionar_forma', 'selecionar')
    else:
      self.btao_selecionar.config(
        text='↖ SELEÇÃO: OFF',
        bg='#3A3D41',
        fg='red',
        relief=RAISED
      )
      self.notificar_controller('desativar_selecao', None)
      self.notificar_controller('selecionar_forma', getattr(self, 'forma_atual', 'reta'))
    

  def menu_ferramentas(self):

    self.btao_selecionar=Button(
      self.f_menu,
      text='↖ SELEÇÃO: OFF',
      bg='#3A3D41',
      fg='#FF6B6B',
      font=('Arial', 9, 'bold'),
      relief=RAISED,
      command=self.alterar_selecao
    )
    self.btao_selecionar.pack(fill=X, padx=10, pady=(15, 5))

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
      text='◯ Borda',
      bg='black',
      fg='white',
      width= 2,
      height= 3,
      relief=FLAT,
      command=lambda: self.abrir_paleta("borda")
    )

    self.btao_cor_borda.pack(fill=X, padx=10, pady=4)

    self.btao_cor_preenchimento = Button(
      self.f_menu,
      text='◉ Preenchimento',
      bg='black',
      fg='white',
      width= 2,
      height= 3,
      relief=FLAT,
      command=lambda: self.abrir_paleta('preenchimento')
    )

    self.btao_cor_preenchimento.pack(fill=X, padx=10, pady=4)


  def menu_visualizacao(self):

    Button(
      self.f_menu,
      text="Limpar Tela",
      bg="#8a2e2e",
      fg='white',
      relief=FLAT,
      command=lambda:
        self.notificar_controller('limpar_tela', None)
    ).pack(side=BOTTOM, fill=X, padx=10, pady=20)

  def menu_camadas(self):
    Label(
      self.f_menu,
      text='▤ CAMADAS',
      bg="#3A3A3A",
      fg="white",
      font=('Arial', 10, 'bold')
      ).pack(pady=(20,8))

    Button(
      self.f_menu,
      text="⏬ Trazer p/ Frente",
      bg="#3A3D41",
      fg='white',
      relief=FLAT,
      command=lambda:
      self.notificar_controller('frente', None)
      ).pack(fill=X, padx=10,pady=4)

    Button(
      self.f_menu,
      text='⏫ Jogar p/ Tras',
      bg="#3A3D41",
      fg='white',
      relief=FLAT,
      command=lambda:
      self.notificar_controller('tras', None)
      ).pack(fill=X, padx=10, pady=4)
    

 
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


  def redesenhar(self, figuras_pronta, figura_atual=None, figura_selecionada=None):
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
     # Linha tracejada na selecao 
      if figura_selecionada is not None and figura == figura_selecionada:
        if hasattr(renderizador, 'desenhar_selecao'):
          renderizador.desenhar_selecao(self.canvas, figura)

    # Desenhar preview da figura atual
    if figura_atual is not None:
      renderizador = CriarRenderizadores.criar(figura_atual)
      renderizador.desenhar_preview(
        self.canvas,
        figura_atual,
        self._cores
      )

  def desenhar_preview_laco(self, pontos):

    if len (pontos) < 2:
      return
    self.canvas.create_line(
      *pontos,
      fill='lightblue',
      dash=(4, 4),
      smooth=True,
      width=2,
      tags='temporario_laco'
    )
  

  def caminho_salvar_png(self):

    return filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Imagem PNG", "*.png")]
    )




  def barra_menu (self): # menu do botão direito do mouse
      barra_menu = Menu(self.root)

      # Arquivo
      menu_arquivo = Menu(barra_menu, tearoff=0)
      menu_arquivo.add_command(
          label="Abrir Projeto",
          command=lambda: self.notificar_controller("abrir", None)
      )
      menu_arquivo.add_command(
          label="Salvar Projeto",
          command=lambda: self.notificar_controller("salvar", None)
      )
      menu_arquivo.add_separator()
      menu_arquivo.add_command(
          label="Sair",
          command=self.root.quit
      )
      barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

      # Formas
      menu_formas = Menu(barra_menu, tearoff=0)

      formas = [
          ("Reta", "reta"),
          ("Mão Livre", "maolivre"),
          ("Círculo", "circulo"),
          ("Retângulo", "retangulo"),
          ("Quadrado", "quadrado"),
          ("Elipse", "elipse"),
          ("Selecionar", "selecionar")
      ]

      for nome, ident in formas:
          menu_formas.add_command(
              label=nome,
              command=lambda f=ident:
                  self.notificar_controller("selecionar_forma", f)
          )

      barra_menu.add_cascade(label="Formas", menu=menu_formas)


      # Sobre
      menu_sobre = Menu(barra_menu, tearoff=0)
      menu_sobre.add_command(
          label="Sobre",
          command=lambda: self.sobre_projeto
      )

      barra_menu.add_cascade(label="Sobre", menu=menu_sobre)

      self.root.config(menu=barra_menu)
      
      
  def menu_contexto(self, event):

    menu = Menu(self.root, tearoff=0)

    menu.add_command(
      label='Recortar',
      command=lambda:
      self.notificar_controller('recortar', None)
    )

    menu.add_command(
        label="Copiar",
        command=lambda:
            self.notificar_controller("copiar", None)
    )

    menu.add_command(
        label="Colar",
        command=lambda:
            self.notificar_controller("colar", None)
    )

    menu.add_separator()

    menu.add_command(
        label="Trazer para frente",
        command=lambda:
            self.notificar_controller("frente", None)
    )

    menu.add_command(
        label="Enviar para trás",
        command=lambda:
            self.notificar_controller("tras", None)
    )

    menu.add_separator()

    menu.add_command(
        label="Apagar",
        command=lambda:
            self.notificar_controller("apagar", None)
    )

    # exibe o menu na tela na posição que o mouse clicou
    menu.tk_popup(event.x_root, event.y_root) # ao inves de funcionar apenas no canvas funciona em toda a tela do paint o comando
    
