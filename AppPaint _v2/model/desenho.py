class Desenho:
    def __init__(self):
        self.figuras = []

    def adicionar(self, figura):#coloca figuras na lista
        self.figuras.append(figura)

    def get_figuras(self):
        return self.figuras.copy()#entrega copia da lista pra evitar de alterar a original

    def clear(self):#limpa figuras
        self.figuras.clear()

    def set_figuras(self, new_fig):
        self.figuras.clear()
        self.figuras.extend(new_fig)

    def apagar (self, figura):
        self.figuras.remove(figura)
     
     # apaga a  figura para depois inserir ela no fundo das outras
    def jogar_para_tras(self, figura):
        self.figuras.remove(figura)
        self.figuras.insert(0, figura)
    
    # apaga a figura para depois inserir ela na frente das outras
    def trazer_para_frente(self, figura):
        self.figuras.remove(self, figura)
        self.figuras.append(figura)
        
        
    def buscar_figura(self, x, y):
        for figura in reversed(self.figuras):
            if figura.contem_ponto(x,y):
                return figura
        
        return None
    
