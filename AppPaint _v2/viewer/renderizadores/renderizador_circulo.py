from viewer.renderizador import Renderizador


class RenderizadorCirculo(Renderizador):
  '''
  Classe responsável por desenhar círculos.
  '''

  @staticmethod
  def desenhar(canvas, circulo, cores):
    '''
    Desenha um círculo.
    '''

    canvas.create_oval(
      *circulo.limites,
      outline= cores.cor_borda,
      fill= cores.cor_preenchimento
    )

  @staticmethod
  def desenhar_preview(canvas, circulo, cores, dash=(4, 2)):
    '''
    Desenha o preview do círculo.
    '''

    canvas.create_oval(
      *circulo.limites,
      outline= cores.cor_borda,
      fill= cores.cor_preenchimento,
      dash= dash
    )
