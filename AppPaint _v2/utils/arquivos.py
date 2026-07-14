import pickle

class Paint_arq:
    
    def salve_arq(self, caminho_arq, figura_salva):
        # salvar as figuras em binario
       try:
            with open(caminho_arq, 'wb') as arq:
                pickle.dump(figura_salva, arq)
            return True
       except Exception as e:
           print(f"ERRROR ao salvar: {e}")
           return False

    def abrir_arq(self, caminho_arq):
# abrir arquivo em binaro
        try:
            with open(caminho_arq, 'rb') as arq:
                figuras = pickle.load(arq)
            return figuras
        
        except Exception as e:
            print(f"ERROR ao abrir: {e}")
        return None

    
