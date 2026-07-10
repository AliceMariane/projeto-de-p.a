from utils.cores import Cores
from viewer.janela import Janela
from controller.criar_figuras import CriarFiguras
from dataclasses import dataclass, field
from model.desenho import Desenho
from model.figura import Figura

#a classe desenho armazena as figuras
@dataclass


class ControladorPrincipal:
  
  _desenho_atual: Figura | None = None #default
  _desenho:str = 'reta' #figura padrao
  _cores: Cores= field(default_factory= Cores) #cores para as figuras
  _janela : Janela| None=None
  _model: Desenho = field(default_factory= Desenho)
        
  def iniciar_fig(self,x,y): #figura que esta sendo criado pelo usuario
    self._desenho_atual= CriarFiguras.criar(
                                        self._desenho,
                                        x,
                                        y,
                                        self._cores._cor_borda,
                                        self._cores._cor_preenchimento
            )
    
  def iniciar_fig(self, x, y):
     self._desenho_atual = CriarFiguras.criar(
        self._desenho,
        x, y,
        self._cores._cor_borda,
        self._cores._cor_preenchimento
     )

  def update_fig(self, x, y):#atualizar figura atual
      if self._desenho_atual:
        self._desenho_atual.atualizar(x, y)
      self._janela.redesenhar(self._model.get_figuras())

  def incluir_newfig (self):#guardar e deixar na tela os desenhos que estao prontos
    if self._desenho_atual:
        self._model.adicionar(self._desenho_atual)
        self._desenho_atual = None

    self._janela.redesenhar(self._model.get_figuras())

    
  def clean_all(self):#manda apagar todos desenhos da tela
    self._model.clear()
    self._desenho_atual = None
    self._janela.redesenhar(self._model.get_figuras())

# funcao cores 
  def set_cor(self, tipo, cor):
  
       if tipo == 'linha':
          self._cores._cor_borda = cor
       elif tipo == 'fundo':
          self._cores_cor_preenchimento = cor

  def set_fig(self, forma):
     self._desenho = forma

     

  #aciona que funcao deve ser 'chamada' para cada acao
  def notificar(self, acao, valor):

    acoes = {
        "selecionar_forma": lambda: self.set_fig(valor),
        "limpar_tela": self.clean_all,
        "mudar_estilo": lambda: self.mudar_estilo(valor),
        "selecionar_ferramenta": lambda: self.selecionar_ferramenta(valor),
        "zoom": lambda: self.zoom(valor),
        "inicio": lambda: self.iniciar_fig(*valor),
        "arrastar": lambda: self.update_fig(*valor),
        "fim": self.incluir_newfig,
        "mudar_cor": lambda: self.set_cor(*valor)
    }

    funcao = acoes.get(acao)

    if funcao:
        funcao()
  
