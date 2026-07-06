from utils.cores import Cores
from viewer.janela import Janela
from controller.criar_figuras import CriarFiguras
from dataclasses import dataclass, field
from model.desenho import Desenho
from model.figura import Figura

#sera necessario criar a classe desenho no model para guardar e apagar os desenhos
@dataclass


class ControladorPrincipal:
  
  #_figuras: list= field(default_factory=list) #armazenar figuras
  _desenho_atual: Figura | None = None #default
  _desenho:str = 'reta' #figura padrao
  _cores: Cores= field(default_factory= Cores) #cores para as figuras
  _janela : Janela= field(default_factory= Janela)
  _model: Desenho = field(default_factory= Desenho)
        
  def iniciar_fig(self,x,y):
    self._desenho_atual= CriarFiguras.criar(
                                        self._desenho,
                                        x,
                                        y,
                                        self._cores.cor_linha,
                                        self._cores.cor_de_preenchimento
            )
    
    
    

  def update_fig(self, x, y):
       if self._desenho_atual:
        self._desenho_atual.update(x, y)

        figuras = self._model.get_figuras + [self._desenho_atual]
        self._janela.redesenhar(figuras)
          
  def incluir_newfig (self):
    if self._desenho_atual:
        self._model.adicionar(self._desenho_atual)
        self._desenho_atual = None

    self._janela.redesenhar(self._model.get_figuras())

  def set_fig (self,desenho):
    self._desenho=desenho
    
  def clean_all(self):
    self._model.clear()
    self._desenho_atual = None
    self._janela.redesenhar(self._model.figuras)
