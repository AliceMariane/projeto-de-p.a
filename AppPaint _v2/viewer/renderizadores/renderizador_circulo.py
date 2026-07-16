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
      outline= circulo.cor_borda,
      fill= circulo.cor_preenchimento
    )

  @staticmethod
  def desenhar_preview(canvas, circulo, cores, dash=(4, 2)):
    '''
    Desenha o preview do círculo.
    '''

    canvas.create_oval(
      *circulo.limites,
      outline= circulo.cor_borda,
      fill= circulo.cor_preenchimento,
      dash= dash
    )

  @staticmethod
  def desenhar_selecao(canvas, circulo):

    '''
    Contorno do circulo
    '''
    canvas.create_oval(
      *circulo.limites,
      outline='black',
      dash=(4, 4),
      width=2
    )

