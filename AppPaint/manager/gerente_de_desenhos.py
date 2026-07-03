#a fabrica tá na mesma pasta de gerente de desenhos
from fabrica_de_figuras import FabricaDeFiguras


class GerenteDeDesenhos:
    '''
    define os desenhos, desenhar é legal quando é voce desenha no papel, 
    mas quando eh voce que faz o papel eh outra historia
'''
    def __init__(self, canvas, gerente_de_cores): #percebi que parte do que tem aqui tinha no main
        self.figuras= []#armazenar figuras
        self.canvas=canvas #os desenhos serao feitos aqui
        self.desenho_atual= None
        self.desenho= 'reta'#padrao, iria preferir que fosse rabisco, talvez troque pra rabisco depois
        self.gerente_de_cores= gerente_de_cores
        
    def iniciar_figura(self, event): #usa a fabrica pra montar o desenhos com os ingredientes 
        self.desenho_atual= FabricaDeFiguras.criar(
            self.desenho,
            event.x,
            event.y,
            self.gerente_de_cores.cor_borda,
            self.gerente_de_cores.cor_preenchimento
            
        )
        
    def update_fig(self,event):
        if self.desenho_atual:
          self.desenho_atual.update( event.x, event.y)
          self.desenhar_fig()
        
    def incluir_figura_nova(self,event):
        if self.desenho_atual:
            self.figuras.append((self.desenho_atual)) # salva a figura junto com a cor
        self.desenhar_fig()
    
    def desenhar_fig (self):
        #desenha as figuras que estao prontas
        self.canvas.delete('all')#os desenhos estao guardados mas a tela apaga
        
        for desenho in self.figuras:#redesenha na tela os desenhos que estao guardados
            desenho.desenhar(self.canvas)
        
        #figuras novas(se desenho atual nao for nada)
        #if self.desenho_atual
        if self.desenho_atual is not None:
            self.desenho_atual.desenhar(self.canvas)
            self.desenho_atual = None
        self.desenhar_fig()
        
    def clean_all (self):#limpa a tela
        self.figuras.clear()
        self.canvas.delete("all")
        print("Tela limpa")
