from viewer.renderizador import Renderizador


class RenderizadorReta(Renderizador):
  '''
  Responsável por desenhar retas.
  '''

  @staticmethod
  def desenhar(canvas, reta, cores):
    '''
    Desenha a reta.
    '''

    canvas.create_line(
      *reta.pontos,
      fill= cores.cor_borda
    )

  @staticmethod
  def desenhar_preview(canvas, reta, cores, dash=(4, 2)):
    '''
    Desenha o preview da reta.
    '''

    canvas.create_line(
      *reta.pontos,
      fill= cores.cor_borda,
      dash= dash
    )
