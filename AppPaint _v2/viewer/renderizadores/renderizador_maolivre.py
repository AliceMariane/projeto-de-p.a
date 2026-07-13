from viewer.renderizador import Renderizador


class RenderizadorMaoLivre(Renderizador):
  '''
  Classe responsável por desenhar
  figuras à mão livre.
  '''

  @staticmethod
  def desenhar(canvas, figura, cores):
    '''
    Desenha o rabisco.
    '''

    canvas.create_line(
      figura.pontos,
      fill= cores.cor_borda,
      smooth= True
    )

  @staticmethod
  def desenhar_preview(canvas, figura, cores, dash=(4, 2)):
    '''
    Desenha o preview do rabisco.
    '''

    canvas.create_line(
      figura.pontos,
      fill= cores.cor_borda,
      smooth= True
    )
