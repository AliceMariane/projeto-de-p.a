class Figura:
    """
    Classe base para todas as figuras.

    Toda figura tem:
        > cor da borda
        > cor do preenchimento
        
    Toda figura pode:
        > ser desenhada
        > ser atualizada enquanto o mouse está pressionado
        > verificar se está incompleta

    Cada subclasse irá implementar sua própria forma de desenhar e atualizar.
    """

    def __init__(self, cor_borda= "black", cor_preenchimento= ""):
        """
        Atributos de classe:

        Parâmetros
        ----------
        cor_borda : str
            Cor da Borda.

        cor_preenchimento : str
            Cor do Preenchimento.
        """

        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def atualizar(self, x, y):
        """
        Atualiza o ultimo ponto (x, y) da figura
        Será implementado pelas subclasses
        """
        pass

    def desenhar(self, canvas):
        """
        Desenha a figura
        Será implementado pelas subclasses
        """
        pass

    def desenhar_preview(self, canvas):
        """
        Preview da figura atual
        """
        pass

    def incompleta(self):
        """
        Verifica se a figura pode ser salva
        """
        return False
