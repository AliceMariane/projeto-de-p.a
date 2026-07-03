from Figuras.reta import Reta
from Figuras.circulo import Circulo
from Figuras.elipse import Elipse
from Figuras.mao_livre import MaoLivre
from Figuras.retangulo import Retangulo
from Figuras.quadrado import Quadrado


class FabricaDeFiguras:
    '''
    cria os objetos das classes de figuras de acordo com a escolha do usuario
    '''
    
    @staticmethod
    def criar (desenho,x, y, cor_borda, cor_preenchimento):

        # estrutura----> if desenho == 'n', return a classe N com o que 'n' usa
        if desenho=='Reta':
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
        
        
#aparentemente a classe Figura eh um asset para estruturar classes de figuras futuras
#poxa essa classe aqui parece a mais facil :/
