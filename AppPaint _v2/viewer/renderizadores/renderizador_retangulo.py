from viewer.renderizador import Renderizador


class RenderizadorRetangulo(Renderizador):
  '''
  Classe responsável por desenhar retângulos.
  '''

  @staticmethod
  def desenhar(canvas, retangulo, cores):
    '''
    Desenha um retângulo.
    '''

    canvas.create_rectangle(
      *retangulo.pontos,
      outline= cores.cor_borda,
      fill= cores.cor_preenchimento
    )

  @staticmethod
  def desenhar_preview(canvas, retangulo, cores, dash=(4, 2)):
    '''
    Desenha o preview do retângulo.
    '''

    canvas.create_rectangle(
      *retangulo.pontos,
      outline= cores.cor_borda,
      fill= cores.cor_preenchimento,
      dash= dash
    )
