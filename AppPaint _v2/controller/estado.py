from abc import ABC, abstractmethod



class Estado(ABC):

    ''' 
    define o comportamento comum das ferramentas
    quando o usuario interage com o canvas
    '''
    
    @abstractmethod
    def clicar (self, controlador_principal,event):
        pass
    
    
    @abstractmethod
    def arrastar (self, controlador_principal, event):
        pass
    
    @abstractmethod
    def soltar (self, controlador_principal, event):
        pass
