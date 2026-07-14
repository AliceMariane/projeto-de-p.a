from abc import ABC, abstractmethod



class Estado(ABC):

  ''' define o comportamento comum das ferramentas
      quando o usuario interage com o canvas
  '''
  @abstractmethod
  def clicar (self, controlador, x, y):
        pass
    
    
  @abstractmethod
  def arrastar (self, controlador, x, y):
        pass

  
  @abstractmethod
  def soltar (self, controlador):
        pass

  
  def copiar_figura(self):
        pass

  
  def colar_figura(self):
        pass
  
  
  def trazer_para_frente(self):
        pass
  

  def jogar_para_tras(self):
        pass
