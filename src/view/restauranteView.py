
class RestauranteView:
    def introduction_page(self):
        message = '''
            Sistema Restaurante

            * 1. Listar Restaurantes 
            * 2. Inserir Prato 
            * 3. Inserir Bebida
            * 4. Listar Cardápio
            * 5. Incluir Restaurante
            * 6. Sair 
        '''
        print(message)
        command = int(input('Comando: '))
        return command

    def obter_detalhes_prato(self):
        item = input("Informe o nome do prato: ")
        preco = float(input("Informe o valor do prato: "))
        descricao = input("Informe a descrição do prato: ")
        return item, preco, descricao

    def obter_detalhes_bebida(self):
        item = input("Informe o nome da bebida: ")
        preco = float(input("Informe o valor da bebida: "))
        descricao = input("Informe a descrição da bebida: ")
        return item, preco, descricao

    def mostrar_resultado(self, resultado):
        print(resultado)
        
    def obter_detalhes_restaurante(self):
        nome = input("Informe o nome do restaurante: ")
        tipo = input("Informe o tipo do restaurante: ")
        return nome, tipo