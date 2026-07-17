
from dataclasses import dataclass, field

from controller.clipboard import Clipboard
from controller.criar_figuras import CriarFiguras
from controller.estado import Estado
from controller.estados.estado_formas import EstadoFormas
from controller.estados.estado_maolivre import EstadoMaoLivre
from controller.estados.estado_selecionar import EstadoSelecionar
from controller.ordenacao import Ordenacao
from controller.selecao import Selecao

from model.desenho import Desenho
from model.figura import Figura

from utils.arquivos import Paint_arq
from utils.cores import Cores

from viewer.janela import Janela


# a classe desenho armazena as figuras
@dataclass
class ControladorPrincipal:

    # ===========================
    # Estado da aplicação
    # ===========================

    _desenho_atual: Figura | None = None  # default
    _desenho: str = 'reta'                # figura padrão

    # ===========================
    # Interface
    # ===========================

    _janela: Janela | None = None

    # ===========================
    # Modelo
    # ===========================

    _model: Desenho = field(default_factory=Desenho)

    # ===========================
    # Estados
    # ===========================

    _estado: Estado = field(default_factory=EstadoFormas)  # estado padrão
    _selecionar: EstadoSelecionar = field(default_factory=EstadoSelecionar)

    # ===========================
    # Objetos auxiliares
    # ===========================

    _cores: Cores = field(default_factory=Cores)  # cores para as figuras
    _clipboard: Clipboard = field(default_factory=Clipboard)
    _selecao: Selecao = field(default_factory=Selecao)
    _ordenacao: Ordenacao = field(default_factory=Ordenacao)

    # ===========================
    # Movimento
    # ===========================

    _ultimo_x: int = 0
    _ultimo_y: int = 0

    # =====================================================
    # DESENHO DAS FIGURAS
    # =====================================================

    def iniciar_fig(self, x, y):

        self._desenho_atual = CriarFiguras.criar(
            self._desenho,
            x,
            y,
            self._cores.cor_borda,
            self._cores.cor_preenchimento
        )

    def update_fig(self, x, y):

        if self._desenho_atual:
            self._desenho_atual.atualizar(x, y)

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras(),
                self._desenho_atual
            )

    def incluir_newfig(self):

        if self._desenho_atual:
            self._model.adicionar(self._desenho_atual)
            self._desenho_atual = None

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras()
            )

    def clean_all(self):
        # manda apagar todos desenhos da tela

        self._model.clear()
        self._desenho_atual = None

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras()
            )
            
    # =====================================================
    # CONFIGURAÇÕES
    # =====================================================

    # função cores
    def set_cor(self, tipo, cor):

        if tipo == 'borda':
            self._cores.cor_borda = cor

        elif tipo == 'preenchimento':
            self._cores.cor_preenchimento = cor

    def set_fig(self, forma):

        estado_generico = EstadoFormas()

        estados = {
            "reta": estado_generico,
            "retangulo": estado_generico,
            "circulo": estado_generico,
            "quadrado": estado_generico,
            "elipse": estado_generico,
            "maolivre": EstadoMaoLivre(),
            "selecionar": self._selecionar
        }

        self._desenho = forma
        self._estado = estados[forma]

    # =====================================================
    # SELEÇÃO E MOVIMENTAÇÃO
    # =====================================================

    def selecionar_figura(self, x, y):
        '''
        Seleciona a figura localizada na posição do mouse.
        '''

        figura = self._model.buscar_figura(x, y)

        self._selecao.selecionar(figura)

        self._ultimo_x = x
        self._ultimo_y = y

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras(),
                None,
                self._selecao.figura
            )

    def mover_figura(self, x, y):
        '''
        Move a figura atualmente selecionada.
        '''

        if not self._selecao.existe():
            return

        dx = x - self._ultimo_x
        dy = y - self._ultimo_y

        self._selecao.figura.mover(dx, dy)

        self._ultimo_x = x
        self._ultimo_y = y

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras(),
                None,
                self._selecao.figura
            )

    def finalizar_movimento(self):
        '''
        Finaliza a movimentação da figura selecionada.
        '''

        pass

    def desativar_selecao(self):

        self._selecao.limpar()
        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras()
            )

    def limpar_selecao(self):

        self._selecao.limpar()
        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras()
            )

    def selecionar_figuras_no_centro(self, pontos):

        if not pontos or len(pontos) < 3:
            return

        poligono_selecao = pontos + [pontos[0]]
        self._selecao.limpar()

        figuras = list(self._model.get_figuras())
        figuras.reverse()

        for figura in figuras:
            px, py = figura.centro if hasattr(figura, 'centro') else (figura.x, figura.y)

            if self._ponto_em_poligono(px, py, poligono_selecao):
                self._selecao.selecionar(figura)
                break

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras(),
                None,
                self._selecao.figura
            )
    @staticmethod
    def pontos_no_poligono(x, y, poligono):
        '''
        Implementar algoritimo de cruzamento de raios para que os pontos estejao no poligono
        '''
        n = len(poligono)
        dentro = False
        p1x, p1y = poligono[0]

        for i in range(n+1):
            p2x, p2y = poligono[i % n]
            if y > min(p1y, p2y):
                if y <= max (p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinter = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinter:
                            dentro = not dentro
            p1x, p1y = p2x, p2y
        return dentro

        # =====================================================
    # OPERAÇÕES SOBRE FIGURAS
    # =====================================================

    def copiar(self):
        '''
        Copia a figura atualmente selecionada
        para a área de transferência.
        '''

        # clipboard == area de transferencia
        self._clipboard.copiar(
            self._selecao.figura
        )

    def colar(self):
        '''
        Cola uma nova cópia da figura
        armazenada na área de transferência.
        '''

        nova_figura = self._clipboard.colar()

        if nova_figura is None:
            return

        self._model.adicionar(nova_figura)

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras()
            )

    def apagar(self):
        '''
        Remove a figura atualmente selecionada.
        '''

        if not self._selecao.existe():
            return

        self._model.apagar(
            self._selecao.figura
        )

        self._selecao.limpar()

        if self._janela:
            self._janela.redesenhar(
                self._model.get_figuras()
            )

    def recortar(self):
        '''
        Copia a figura e depois apaga
        '''
        self.copiar()
        self.apagar()

    def trazer_para_frente(self):
        '''
        Move a figura selecionada uma posição para frente.
        '''

        if not self._selecao.existe():
            return

        figuras = self._model.get_figuras()
        
        self._ordenacao.frente(
            figuras ,
            self._selecao.figura
        )
        self._model.set_figuras(figuras) #salva nova ordem das figuras no model

        if self._janela:
            self._janela.redesenhar(
                figuras,
                None,
                self._selecao.figura
            )

    def jogar_para_tras(self):
        '''
        Move a figura selecionada uma posição para trás.
        '''

        if not self._selecao.existe():
            return
        figuras = self._model.get_figuras()
        
        self._ordenacao.tras(
            figuras ,
            self._selecao.figura,
        )
        self._model.set_figuras(figuras) #salva nova ordem das figuras no model
        
        if self._janela:
            self._janela.redesenhar(figuras)

    # =====================================================
    # ARQUIVOS
    # =====================================================

    # adicionando funcao de salvamento e abertura de arquivos
    def executar_salvamento(self):

        caminho_escolhido = self._janela.caminho_salvar()

        if caminho_escolhido:

            figuras = self._model.get_figuras()

            salvador = Paint_arq()

            sucesso = salvador.salve_arq(
                caminho_escolhido,
                figuras
            )

            if sucesso:
                print('Projeto salvo')
            else:
                print('ERROR ao salvar')

    def executar_abrir(self):

        caminho_escolhido = self._janela.caminho_abrir()

        if caminho_escolhido:

            carregador = Paint_arq()

            figuras_carregadas = carregador.abrir_arq(
                caminho_escolhido
            )

            if figuras_carregadas is not None:

                self._model.set_figuras(
                    figuras_carregadas
                )

                if self._janela:
                    self._janela.redesenhar(
                        self._model.get_figuras()
                    )

                print('Projeto aberto')

            else:
                print('ERROR ao abrir')
    
    # =====================================================
    # NOTIFICAÇÕES DA VIEW
    # =====================================================

    # aciona qual função deve ser chamada para cada ação
    def notificar(self, acao, valor):

        # teste ---> print("recebi:", acao)

        acoes = {

            # seleção de ferramenta
            "selecionar_forma": lambda: self.set_fig(valor),
            "desativar_selecao": self.desativar_selecao,

            # desenho
            "inicio": lambda: self._estado.clicar(
                self,
                valor[0],
                valor[1]
            ),

            "arrastar": lambda: self._estado.arrastar(
                self,
                valor[0],
                valor[1]
            ),

            "fim": lambda: self._estado.soltar(self),

            # edição
            "copiar": self.copiar,
            "colar": self.colar,
            "apagar": self.apagar,
            "recortar": self.recortar,

            # ordenação
            "frente": self.trazer_para_frente,
            "tras": self.jogar_para_tras,

            # configurações
            "mudar_cor": lambda: self.set_cor(*valor),

            # arquivo
            "salvar": self.executar_salvamento,
            "abrir": self.executar_abrir,

            # tela
            "limpar_tela": self.clean_all,

            # futuras funcionalidades
            # "mudar_estilo": lambda: self.mudar_estilo(valor),
            # "selecionar_ferramenta": lambda: self.selecionar_ferramenta(valor),
            # "zoom": lambda: self.zoom(valor),
        }

        funcao = acoes.get(acao)

        # teste ---> print("funcao:", funcao)

        if funcao:
            funcao()
        else:
            print(f"Ação desconhecida: {acao}")
