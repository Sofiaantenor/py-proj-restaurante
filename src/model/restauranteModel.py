
class RestauranteModel:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.cardapio_pratos = []
        self.cardapio_bebidas = []

    def incluir_prato_no_cardapio(self, item, preco, descricao):
        prato = {'item': item, 'preco': preco, 'descricao': descricao}
        self.cardapio_pratos.append(prato)

    def incluir_bebida_no_cardapio(self, item, preco, descricao):
        bebida = {'item': item, 'preco': preco, 'descricao': descricao}
        self.cardapio_bebidas.append(bebida)

    def listar_restaurantes(self):
        print(f'Restaurante: {self.nome}, Tipo: {self.tipo}')
        

    def listar_cardapio(self):
        print("Cardápio de Pratos:")
        for prato in self.cardapio_pratos:
            print(f"{prato['item']} - R${prato['preco']}: {prato['descricao']}")
        
        print("\nCardápio de Bebidas:")
        for bebida in self.cardapio_bebidas:
            print(f"{bebida['item']} - R${bebida['preco']}: {bebida['descricao']}")
            
            
class GerenciadorRestaurantes:
    def __init__(self):
        self.restaurantes = []

    def adicionar_restaurante(self, nome, tipo):
        novo_restaurante = RestauranteModel(nome, tipo)
        self.restaurantes.append(novo_restaurante)

    def listar_restaurantes(self):
        if not self.restaurantes:
            print("Nenhum restaurante cadastrado.")
            return
        
        for restaurante in self.restaurantes:
            restaurante.listar_restaurantes()
        input(" digite algo para voltar ao menu")    