from PIL import Image, ImageDraw

from model.reta import Reta
from model.retangulo import Retangulo
from model.quadrado import Quadrado
from model.circulo import Circulo
from model.elipse import Elipse
from model.mao_livre import MaoLivre


class SalvarPNG:

    def salvar(self, caminho, figuras, cores, largura=800, altura=600):

        imagem = Image.new("RGB", (largura, altura), "white")
        draw = ImageDraw.Draw(imagem)

        for figura in figuras:

            if isinstance(figura, Reta):

                draw.line(
                    figura.pontos,
                    fill=cores.cor_borda,
                    width=2
                )

            elif isinstance(figura, Retangulo):

                draw.rectangle(
                    figura.pontos,
                    outline=cores.cor_borda,
                    fill=cores.cor_preenchimento
                )

            elif isinstance(figura, Quadrado):

                draw.rectangle(
                    figura.pontos,
                    outline=cores.cor_borda,
                    fill=cores.cor_preenchimento
                )

            elif isinstance(figura, Circulo):

                draw.ellipse(
                    figura.pontos,
                    outline=cores.cor_borda,
                    fill=cores.cor_preenchimento
                )

            elif isinstance(figura, Elipse):

                draw.ellipse(
                    figura.pontos,
                    outline=cores.cor_borda,
                    fill=cores.cor_preenchimento
                )

            elif isinstance(figura, MaoLivre):

                if len(figura.pontos) > 1:

                    draw.line(
                        figura.pontos,
                        fill=cores.cor_borda,
                        width=2
                    )

        imagem.save(caminho)