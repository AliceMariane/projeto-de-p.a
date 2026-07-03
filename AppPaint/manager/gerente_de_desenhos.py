from fabrica_de_figuras import FabricaDeFiguras

class GerenteDeDesenhos:
    '''
    classe que controla e define os desenhos do paint
'''
    def __init__(self, canvas, gerente_de_cores):
        self.figuras= []#armazenar figuras
        self.canvas=canvas #os desenhos serao feitos no canvas
        self.desenho_atual= None #default
        self.desenho= 'Reta'#figura padrao
        self.gerente_de_cores= gerente_de_cores #cores para as figuras
        
    def iniciar_figura(self, event): #comeca uma figura
        self.desenho_atual= FabricaDeFiguras.criar(
            self.desenho,
            event.x,
            event.y,
            self.gerente_de_cores.cor_borda,
            self.gerente_de_cores.cor_preenchimento
            
        )
        
    def update_fig(self,event):#atualiza a  figura que o usuario esta fazendo e redesenha (desenhar_fig)
        if self.desenho_atual:
          self.desenho_atual.update( event.x, event.y)
          self.desenhar_fig()
        
    def incluir_figura_nova(self,event): 
        if self.desenho_atual:
            self.figuras.append((self.desenho_atual)) # salva a figura junto com a cor
        self.desenhar_fig()
    
    def desenhar_fig (self):
        #desenha na tela as figuras que estao prontas e guardadas
        self.canvas.delete('all')#os desenhos estao guardados, o que apaga pra atualizar eh o que aparece na tela
        
        for desenho in self.figuras:#redesenha na tela os desenhos que estao guardados
            desenho.desenhar(self.canvas)
        
        #quando se desenha figuras novas(se desenho atual nao for nada)
        #if self.desenho_atual
        if self.desenho_atual is not None:
            self.desenho_atual.desenhar(self.canvas)
            self.desenho_atual = None
        self.desenhar_fig()
        
    def clean_all (self):#limpa a tela
        self.figuras.clear()
        self.canvas.delete("all")
        print("Tela limpa")
