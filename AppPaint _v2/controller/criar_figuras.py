#importando as classes de figuras
from model.reta import Reta
from model.circulo import Circulo
from model.elipse import Elipse
from model.mao_livre import MaoLivre
from model.retangulo import Retangulo
from model.quadrado import Quadrado


class  CriarFiguras:
    '''
    cria os objetos das classes de figuras de acordo com a escolha do usuario
    '''
    
    @staticmethod
    def criar (desenho,x, y, cor_borda, cor_preenchimento):

        #Estrura dicionario para as formas
        
        mapa_fig = {
            'reta': Reta,
            'retangulo': Retangulo,
            'circulo': Circulo,
            'elipse': Elipse,
            'quadrado': Quadrado,
            'maolivre': MaoLivre,
        }

        Classefig = mapa_fig.get(desenho, MaoLivre)

        nova_fig = Classefig(x, y)

        nova_fig._cor_borda = cor_borda
        nova_fig._cor_preenchimento = cor_preenchimento

        return nova_fig
