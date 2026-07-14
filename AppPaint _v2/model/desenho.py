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
