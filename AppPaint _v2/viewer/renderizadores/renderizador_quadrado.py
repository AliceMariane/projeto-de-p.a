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
      outline= quadrado.cor_borda,
      fill= quadrado.cor_preenchimento
    )

  @staticmethod
  def desenhar_preview(canvas, quadrado, cores, dash=(4, 2)):
    '''
    Desenha o preview do quadrado.
    '''

    canvas.create_rectangle(
      *quadrado.pontos,
      outline= quadrado.cor_borda,
      fill= quadrado.cor_preenchimento,
      dash= dash
    )

  @staticmethod
  def desenhar_selecao(canvas, quadrado):

    canvas.create_rectangle(
      *quadrado.pontos,
      outline='black',
      dash=(4, 4),
      width=2
    )
