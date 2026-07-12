from viewer.renderizador import Renderizador

class RenderizadorMaoLivre(Renderizador):
    '''
    Classe responsável por desenhar
    figuras à mão livre.
    '''

    @staticmethod
    def desenhar(canvas, figura):
        '''
        Desenha o rabisco.
        '''

        # Desenha todos os pontos armazenados
        # na figura utilizando uma linha suavizada.
        canvas.create_line(
            figura.pontos,
            fill= figura.cor_borda,
            smooth= True
        )

    @staticmethod
    def desenhar_preview(canvas, figura, dash= (4, 2)):
        '''
        Desenha o preview do rabisco.

        Para desenhos à mão livre, o preview é
        igual ao desenho definitivo
        '''

        canvas.create_line(
            figura.pontos,
            fill= figura.cor_borda,
            smooth= True
        )
