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
  _janela : Janela= field(default_factory= Janela)
  _model: Desenho = field(default_factory= Desenho)
        
  def iniciar_fig(self,x,y): #figura que esta sendo criado pelo usuario
    self._desenho_atual= CriarFiguras.criar(
                                        self._desenho,
                                        x,
                                        y,
                                        self._cores.cor_linha,
                                        self._cores.cor_de_preenchimento
            )
    
  def update_fig(self, x, y):#atualizar figura atual
      if self._desenho_atual:
        self._desenho_atual.update(x, y)

        figuras = self._model.get_figuras()+ [self._desenho_atual]
        self._janela.redesenhar(figuras)
          
  def incluir_newfig (self):#guardar e deixar na tela os desenhos que estao prontos
    if self._desenho_atual:
        self._model.adicionar(self._desenho_atual)
        self._desenho_atual = None

    self._janela.redesenhar(self._model.get_figuras())

  def set_fig (self,desenho):#alterar tipo de figura exemplo: 'reta'----->'circulo'
    self._desenho=desenho
    
  def clean_all(self):#manda apagar todos desenhos da tela
    self._model.clear()
    self._desenho_atual = None
    self._janela.redesenhar(self._model.get_figuras())
