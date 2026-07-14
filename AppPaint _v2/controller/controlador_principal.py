from utils.cores import Cores
from utils.arquivos import Paint_arq
from viewer.janela import Janela
from controller.criar_figuras import CriarFiguras
from dataclasses import dataclass, field
from model.desenho import Desenho
from model.figura import Figura
from controller.estado import Estado
from controller.estados.estado_formas import EstadoFormas
from controller.estados.estado_maolivre import EstadoMaoLivre
from controller.estados.estado_selecionar import EstadoSelecionar


# a classe desenho armazena as figuras
@dataclass
class ControladorPrincipal:
  
  _desenho_atual : Figura | None = None # default
  _desenho : str = 'reta' # figura padrão
  _cores : Cores = field(default_factory= Cores) # cores para as figuras
  _janela : Janela | None=None
  _model: Desenho = field(default_factory= Desenho)
  _estado: Estado = field(default_factory= EstadoFormas) # estado padrão

        
  def iniciar_fig(self,x,y): 
    self._desenho_atual= CriarFiguras.criar(
                                      self._desenho,
                                      x, y,
                                      self._cores.cor_borda,
                                      self._cores.cor_preenchimento
                                    )
    
  
  def update_fig(self, x, y): 
    if self._desenho_atual:
      self._desenho_atual.atualizar(x, y)
      
    if self._janela:
      self._janela.redesenhar(
        self._model.get_figuras(),
        self._desenho_atual
    )
    

  def incluir_newfig (self): 
    if self._desenho_atual:
      self._model.adicionar(self._desenho_atual)
      self._desenho_atual = None
     
    if self._janela:
      self._janela.redesenhar(self._model.get_figuras())


  def clean_all(self): # manda apagar todos desenhos da tela
    self._model.clear()
    self._desenho_atual = None
    self._janela.redesenhar(self._model.get_figuras())

# função cores 
  def set_cor(self, tipo, cor):
    if tipo == 'borda':
      self._cores.cor_borda = cor
      
    elif tipo == 'preenchimento':
      self._cores.cor_preenchimento = cor

  def set_fig(self, forma):
    estado_generico = EstadoFormas()
    estados = {
    "reta": estado_generico,
    "retangulo": estado_generico,
    "circulo": estado_generico,
    "quadrado": estado_generico,
    "elipse": estado_generico,
    "maolivre": EstadoMaoLivre(),
    "selecionar": EstadoSelecionar()
    }
    
    self._desenho= forma
    self._estado = estados[forma]
    
    # adicionando funcao de salvamento e abertura de arquivos
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
     
     
  # aciona qual função deve ser 'chamada' para cada ação
  def notificar(self, acao, valor):
    # teste---> print('recebi: ', acao)
    self._estado= EstadoSelecionar
    acoes = {
        "selecionar_forma": lambda: self.set_fig(valor),
        "limpar_tela": self.clean_all,
        # "mudar_estilo": lambda: self.mudar_estilo(valor),
        # "selecionar_ferramenta": lambda: self.selecionar_ferramenta(valor),
        # "zoom": lambda: self.zoom(valor),
        "inicio": lambda: self.iniciar_fig(valor[0], valor[1]),
        "arrastar": lambda: self.update_fig(valor[0], valor[1]),
        "fim": lambda: self.incluir_newfig(),
        "mudar_cor": lambda: self.set_cor(*valor),
        "salvar": self.execultar_salvamento,
        "abrir":  self.execultar_abrir,
        'frente': lambda: self._estado.trazer_para_frente(),
        'tras': lambda: self._estado.jogar_para_tras(),
        'copiar': lambda: self._estado.copiar_figura(),
        'colar': lambda: self._estado.colar_figura(),
        'apagar': None # no momento nao sei como vai funcionar
        }
    funcao = acoes.get(acao)
    # teste---> print('funcao: ', funcao)
    if funcao:
      funcao()
    else:
      print(f"Ação desconhecida: {acao}")
      
