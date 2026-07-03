class GerenteDeCores:   
    ''' 
    Define as cores das figuras
    '''
    def __init__ (self):
        self._cor_borda= 'black' #cor padrao
        self._cor_preenchimento='' #preenchimento inicial/padrao(vazio)
        
    @property
    def cor_atual_da_linha (self):#cor utilizada atualmente na borda/linha das figuras
        return self._cor_borda
    @property
    def cor_atual_do_preenchimento(self):#cor utilizada atualmente no preenchimento das figuras
        return self._cor_preenchimento

    @cor_atual_da_linha.setter
    def color_select_outline(self, nova_cor): #cor que o usuario escolheu para a borda/linha das figuras
        self.cor_borda= nova_cor
    @cor_atual_do_preenchimento.setter
    def color_select_fill(self, nova_cor): #cor que o usuario escolheu para o preenchimento das giguras
        self.cor_preenchimento= nova_cor
