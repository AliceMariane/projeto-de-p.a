from utils.cores import Cores
from viewer.janela import Janela
from controller.criar_figuras import CriarFiguras
from dataclasses import dataclass, field
from model.desenho import Desenho
from model.figura import Figura
from controller.estado import Estado
from controller.estados.estado_reta import EstadoReta
from controller.estados.estado_circulo import EstadoCirculo
from controller.estados.estado_retangulo import EstadoRetangulo
from controller.estados.estado_quadrado import EstadoQuadrado
from controller.estados.estado_elipse import EstadoElipse
from controller.estados.estado_maolivre import EstadoMaoLivre


# a classe desenho armazena as figuras
@dataclass
class ControladorPrincipal:
  
  _desenho_atual : Figura | None = None # default
  _desenho : str = 'reta' # figura padrão
  _cores : Cores = field(default_factory= Cores) # cores para as figuras
  _janela : Janela | None=None
  _model: Desenho = field(default_factory= Desenho)
  _estado: Estado = field(default_factory= EstadoReta) # estado padrão
        
  def iniciar_fig(self,x,y): # figura que está sendo criado pelo usuário
    self._desenho_atual= CriarFiguras.criar(
                                      self._desenho,
                                      x, y,
                                      self._cores.cor_borda,
                                      self._cores.cor_preenchimento
                                    )
    
    if self._desenho_atual is None:
      print(f"Figura '{self._desenho}' não registrada.")
    
  def update_fig(self, x, y): # atualizar figura atual
    if self._desenho_atual:
      self._desenho_atual.atualizar(x, y)
      
    if self._janela:
      self._janela.redesenhar(
        self._model.get_figuras(),
        self._desenho_atual
    )

  def incluir_newfig (self): # guardar e deixar na tela os desenhos que estao prontos
    if self._desenho_atual:
      self._model.adicionar(self._desenho_atual)
      self._desenho_atual = None

    self._janela.redesenhar(self._model.get_figuras())

  def clean_all(self): # manda apagar todos desenhos da tela
    self._model.clear()
    self._desenho_atual = None
    self._janela.redesenhar(self._model.get_figuras())

# função cores 
  def set_cor(self, tipo, cor):
    if tipo == 'linha':
      self._cores.cor_borda = cor
      
    elif tipo == 'fundo':
      self._cores.cor_preenchimento = cor

  def set_fig(self, forma):
    estados = {
    "reta": EstadoReta(),
    "retangulo": EstadoRetangulo(),
    "circulo": EstadoCirculo(),
    "quadrado": EstadoQuadrado(),
    "elipse": EstadoElipse(),
    "maolivre": EstadoMaoLivre()
    }
    
    self._desenho= forma
    self._estado = estados[forma]
    
'''  # adicionando funcao de salvamento e abertura de arquivos
  def execultar_salvamento(self):
    caminho_escolhido = self._janela.caminho_salvar()
    
  if caminho_escolhido:
    figuras = self._model.get_figuras()
    salvador = Paint_arq()
    sucesso = salvador.salve_arq(caminho_escolhido, figuras)
    if sucesso:
        print('Projeto salvo')
    else:
        print('ERROR ao salvar')
          
  def execultar_abrir(self):
    caminho_escolhido = self._janela.caminho_abrir()

    if caminho_escolhido:
        carregador = Paint_arq()
        figuras_carregadas = carregador.abrir_arq(caminho_escolhido)

        if figuras_carregadas is not None:
          self._model.set_figuras(figuras_carregadas)
          self._janela.redesenhar(self._model.get_figuras())
          print('Projeto aberto')
        else:
          print('ERROR ao abrir')
     '''
     
  # aciona qual função deve ser 'chamada' para cada ação
def notificar(self, acao, valor):
  acoes = {
      "selecionar_forma": lambda: self.set_fig(valor),
      "limpar_tela": self.clean_all,
      # "mudar_estilo": lambda: self.mudar_estilo(valor),
      # "selecionar_ferramenta": lambda: self.selecionar_ferramenta(valor),
      # "zoom": lambda: self.zoom(valor),
      "inicio": lambda: self._estado.clicar(self.event),
      "arrastar": lambda: self._estado.arrastar(self.event),
      "fim": lambda: self._estado.soltar(self),
      "mudar_cor": lambda: self.set_cor(*valor),
      "salvar": self.execultar_salvamento,
      "abrir": self.execultar_abrir
      }
  funcao = acoes.get(acao)

  if funcao:
    funcao()
  else:
    print(f"Ação desconhecida: {acao}")
    
