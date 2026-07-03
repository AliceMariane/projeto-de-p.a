from fabrica_de_figuras import FabricaDeFiguras

class GerenteDeDesenhos:
    '''
    classe que controla e define os desenhos do paint
'''
    def __init__(self, canvas, gerente_de_cores):
        self._figuras= []#armazenar figuras
        self._canvas=canvas #os desenhos serao feitos no canvas
        self._desenho_atual= None #default
        self._desenho= 'Reta'#figura padrao
        self._gerente_de_cores= gerente_de_cores #cores para as figuras
        
    def iniciar_figura(self, event): #comeca uma figura
        self._desenho_atual= FabricaDeFiguras.criar(
            self._desenho,
            event.x,
            event.y,
            self._gerente_de_cores.cor_borda,
            self._gerente_de_cores.cor_preenchimento
            
        )
        
    def update_fig(self,event):#atualiza a  figura que o usuario esta fazendo e redesenha (desenhar_fig)
        if self._desenho_atual:
          self._desenho_atual.update( event.x, event.y)
          self.desenhar_fig()
        
    def incluir_figura_nova(self,event): 
        if self._desenho_atual:
            self._figuras.append((self._desenho_atual)) # salva a figura junto com a cor
            self._desenho_atual= None
            
        self.desenhar_fig()
    
    def desenhar_fig (self):
        #desenha na tela as figuras que estao prontas e guardadas
        self._canvas.delete('all')#os desenhos estao guardados, o que apaga pra atualizar eh o que aparece na tela
        
        for desenho in self._figuras:#redesenha na tela os desenhos que estao guardados
            desenho.desenhar(self._canvas)
        
        #quando se desenha figuras novas(se desenho atual nao for nada)
        #if self.desenho_atual
        if self._desenho_atual is not None:
            self._desenho_atual.desenhar(self._canvas)
        #self.desenhar_fig()
        
    def clean_all (self):#limpa a tela
        self._figuras.clear()
        self._canvas.delete("all")
        print("Tela limpa")
