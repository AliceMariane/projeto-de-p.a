# importando as figuras
from model.reta import Reta
from model.retangulo import Retangulo
from model.quadrado import Quadrado
from model.circulo import Circulo
from model.elipse import Elipse
from model.mao_livre import MaoLivre


# importando os renderizadores
from viewer.renderizadores.renderizador_reta import RenderizadorReta
from viewer.renderizadores.renderizador_retangulo import RenderizadorRetangulo
from viewer.renderizadores.renderizador_quadrado import RenderizadorQuadrado
from viewer.renderizadores.renderizador_circulo import RenderizadorCirculo
from viewer.renderizadores.renderizador_elipse import RenderizadorElipse
from viewer.renderizadores.renderizador_mao_livre import RenderizadorMaoLivre


class CriarRenderizadores:
  '''
  Retorna o renderizador correspondente
  ao tipo da figura.
  '''

  @staticmethod
  def criar(figura):
    '''
    Seleciona o renderizador adequado
    para uma figura.
    '''

    mapa_renderizadores = {
      Reta: RenderizadorReta,
      Retangulo: RenderizadorRetangulo,
      Quadrado: RenderizadorQuadrado,
      Circulo: RenderizadorCirculo,
      Elipse: RenderizadorElipse,
      MaoLivre: RenderizadorMaoLivre
    }

    return mapa_renderizadores[type(figura)]
