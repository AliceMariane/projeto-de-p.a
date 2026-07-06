class Cores:   
    ''' 
    Define as cores das figuras
    '''
    
    def __init__(self):
        self._cor_borda= 'black' #cor padrao
        self._cor_preenchimento='' #preenchimento inicial/padrao(vazio)

    @property
    def cor_borda(self): #cor utilizada atualmente na borda/linha das figuras
        return self._cor_borda
    @property
    def cor_preenchimento(self): #cor utilizada atualmente no preenchimento das figuras
        return self._cor_preenchimento

    @cor_borda.setter
    def cor_borda(self, nova_cor): #cor que o usuario escolheu para a borda/linha das figuras
        self._cor_borda = nova_cor

    @cor_preenchimento.setter
    def cor_preenchimento(self, nova_cor): #cor que o usuario escolheu para o preenchimento das giguras
        self._cor_preenchimento = nova_cor
