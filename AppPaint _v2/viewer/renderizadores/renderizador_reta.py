from viewer.renderizador import Renderizador


class RenderizadorReta(Renderizador):
    '''
    Responsável por desenhar retas.
    '''

    @staticmethod
    def desenhar(canvas, reta):
        '''
        Desenha a reta.
        '''

        canvas.create_line(
            *reta.pontos,
            fill= reta.cor_borda
        )

    @staticmethod
    def desenhar_preview(canvas, reta, dash=(4, 2)):
        '''
        Desenha o preview da reta.
        '''

        canvas.create_line(
            *reta.pontos,
            fill= reta.cor_borda,
            dash= dash
        )
