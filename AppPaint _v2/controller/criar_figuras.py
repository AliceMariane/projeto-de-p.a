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

        # estrutura----> if desenho == 'n', return a classe N com o que 'n' usa
        
        if desenho=='Reta':#se a figura for reta
            return Reta(x,y,cor_borda)
        
        elif desenho=='Retangulo':
            return Retangulo(x,y,cor_borda,cor_preenchimento)
        
        elif desenho=='Circulo':
            return Circulo(x,y,cor_borda, cor_preenchimento)
        
        elif desenho=='Elipse':
            return Elipse(x,y,cor_borda, cor_preenchimento)
        
        elif desenho=='Quadrado':
            return Quadrado(x,y,cor_borda, cor_preenchimento)
        
        else:#desenha a mao livre==rabisco
            return MaoLivre(x,y,cor_borda)
