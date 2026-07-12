from viewer.renderizador import Renderizador


class RenderizadorElipse(Renderizador):
    '''
    Classe responsável por desenhar elipses.
    '''

    @staticmethod
    def desenhar(canvas, elipse):
        '''
        Desenha uma elipse.
        '''

        canvas.create_oval(
            elipse.ini_x,
            elipse.ini_y,
            elipse.fim_x,
            elipse.fim_y,
            outline=elipse.cor_borda,
            fill=elipse.cor_preenchimento
        )

    @staticmethod
    def desenhar_preview(canvas, elipse, dash=(4, 2)):
        '''
        Desenha o preview da elipse.
        '''

        canvas.create_oval(
            elipse.ini_x,
            elipse.ini_y,
            elipse.fim_x,
            elipse.fim_y,
            outline=elipse.cor_borda,
            fill='',
            dash=dash
        )
