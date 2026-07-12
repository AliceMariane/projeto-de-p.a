from viewer.renderizador import Renderizador


class RenderizadorCirculo(Renderizador):
    '''
    Classe responsável por desenhar círculos.
    '''

    @staticmethod
    def desenhar(canvas, circulo):
        '''
        Desenha um círculo.
        '''

        canvas.create_oval(
            circulo.cx - circulo.raio,
            circulo.cy - circulo.raio,
            circulo.cx + circulo.raio,
            circulo.cy + circulo.raio,
            outline=circulo.cor_borda,
            fill=circulo.cor_preenchimento
        )

    @staticmethod
    def desenhar_preview(canvas, circulo, dash=(4, 2)):
        '''
        Desenha o preview do círculo.
        '''

        canvas.create_oval(
            circulo.cx - circulo.raio,
            circulo.cy - circulo.raio,
            circulo.cx + circulo.raio,
            circulo.cy + circulo.raio,
            outline=circulo.cor_borda,
            fill='',
            dash=dash
        )
