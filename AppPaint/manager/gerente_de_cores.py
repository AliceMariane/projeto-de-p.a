class GerenteDeCores:   
    ''' 
    Define as cores das figuras
    '''
    def __init__ (self):
        self.cor_borda= 'black' #cor padrao, pra que seria rosa?
        self.cor_preenchimento=''
        
        
    def color_select_outline(self, nova_cor): #cor que o usuario escolheu
        self.cor_borda= nova_cor

    def color_select_fill(self, nova_cor): #cor que o usuario escolheu
        self.cor_preenchimento= nova_cor
        
    def wtfIsThisColor (self):
        return self.cor_borda #a cor que vai usar nas figuras
    
    def cor_atual_da_linha (self):
        return self.wtfIsThisColor()

    def cor_atual_do_preenchimento(self):
        return self.cor_preenchimento


#talvez eu volte aqui
        
