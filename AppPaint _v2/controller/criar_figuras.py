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
    def criar (desenho,x, y, _cor_borda, _cor_preenchimento):

        # estrutura----> if desenho == 'n', return a classe N com o que 'n' usa
        
        if desenho=='reta':#se a figura for reta
            return Reta(x,y,_cor_borda)
        
        elif desenho=='retangulo':
            return Retangulo(x,y,_cor_borda,_cor_preenchimento)
        
        elif desenho=='circulo':
            return Circulo(x,y,_cor_borda, _cor_preenchimento)
        
        elif desenho=='elipse':
            return Elipse(x,y,_cor_borda, _cor_preenchimento)
        
        elif desenho=='quadrado':
            return Quadrado(x,y,_cor_borda, _cor_preenchimento)
        
        else:#desenha a mao livre==rabisco
            return MaoLivre(x,y, _cor_borda)
