# Responsabilidade única

class SistemaCadastral:
    
    def cadastrar(self, nome:str, idade:int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()
            
    def __verificar_dados(self, nome:str, idade:int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
            
    def __armazenar_usuario(self, nome:str, idade:int) -> None:
        print("Acessando...")
        print(f"Cadastrar usuário {nome}, idade {idade}")
        
    def __indicar_erro(self):
        print("Dados inválidos.")
    