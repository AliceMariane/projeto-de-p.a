# importando as classes de figuras
from model.reta import Reta
from model.circulo import Circulo
from model.elipse import Elipse
from model.mao_livre import MaoLivre
from model.retangulo import Retangulo
from model.quadrado import Quadrado


class CriarFiguras:
  '''
  Cria os objetos das classes de figuras
  de acordo com a escolha do usuário.
  '''

  @staticmethod
  def criar(desenho, x, y):
    '''
    Cria uma nova figura.
    '''

    # Estrutura dicionário para as formas

    mapa_fig = {
      'reta': Reta,
      'retangulo': Retangulo,
      'circulo': Circulo,
      'elipse': Elipse,
      'quadrado': Quadrado,
      'maolivre': MaoLivre,
    }

    classe_fig = mapa_fig.get(desenho, MaoLivre)

    nova_fig = classe_fig(x, y)
    
    return nova_fig
