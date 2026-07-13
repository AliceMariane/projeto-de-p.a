from viewer.renderizador import Renderizador


class RenderizadorQuadrado(Renderizador):
  '''
  Classe responsável por desenhar quadrados.
  '''

  @staticmethod
  def desenhar(canvas, quadrado, cores):
    '''
    Desenha um quadrado.
    '''

    canvas.create_rectangle(
      *quadrado.pontos,
      outline= cores.cor_borda,
      fill= cores.cor_preenchimento
    )

  @staticmethod
  def desenhar_preview(canvas, quadrado, cores, dash=(4, 2)):
    '''
    Desenha o preview do quadrado.
    '''

    canvas.create_rectangle(
      *quadrado.pontos,
      outline= cores.cor_borda,
      fill= cores.cor_preenchimento,
      dash= dash
    )
