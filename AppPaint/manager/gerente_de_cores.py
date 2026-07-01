class GerenteDeCores:   
    ''' 
    define as cores das figuras
'''
    def __init__ (self):
        self.cor= 'black' #cor padrao, pra que seria rosa?
        
    def color_select(self, novaCor): #cor que o usuario escolheu
        self.cor= novaCor
        
    def wtfIsThisColor (self):
        return self.cor #a cor que vai usar nas figuras
    
    def corAtual (self):
        return self.wtfIsThisColor()
        