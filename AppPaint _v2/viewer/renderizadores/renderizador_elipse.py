from viewer.renderizador import Renderizador


class RenderizadorElipse(Renderizador):
  '''
  Classe responsável por desenhar elipses.
  '''

  @staticmethod
  def desenhar(canvas, elipse, cores):
    '''
    Desenha uma elipse.
    '''

    canvas.create_oval(
      *elipse.pontos,
      outline= elipse.cor_borda,
      fill= elipse.cor_preenchimento
    )

  @staticmethod
  def desenhar_preview(canvas, elipse, cores, dash=(4, 2)):
    '''
    Desenha o preview da elipse.
    '''

    canvas.create_oval(
      *elipse.pontos,
      outline= elipse.cor_borda,
      fill= elipse.cor_preenchimento,
      dash= dash
    )
