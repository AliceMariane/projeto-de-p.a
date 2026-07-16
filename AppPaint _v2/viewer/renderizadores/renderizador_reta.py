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
      fill= reta.cor_borda
    )

  @staticmethod
  def desenhar_preview(canvas, reta, cores, dash=(4, 2)):
    '''
    Desenha o preview da reta.
    '''

    canvas.create_line(
      *reta.pontos,
      fill= reta.cor_borda,
      dash= dash
    )


  @staticmethod
  def desenhar_selecao(canvas, reta):

    canvas. create_line(
      *reta.pontos,
      fill='black', 
      dash=(4, 4),
      width=2
    )
