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
      outline= retangulo.cor_borda,
      fill= retangulo.cor_preenchimento
    )

  @staticmethod
  def desenhar_preview(canvas, retangulo, cores, dash=(4, 2)):
    '''
    Desenha o preview do retângulo.
    '''

    canvas.create_rectangle(
      *retangulo.pontos,
      outline= retangulo.cor_borda,
      fill= retangulo.cor_preenchimento,
      dash= dash
    )

  @staticmethod
  def desenhar_selecao(canvas, retangulo):

    canvas.create_rectangle(
      *retangulo.pontos,
      outline='black',
      dash=(4, 4),
      width=2
    )
