
from model.restauranteModel import GerenciadorRestaurantes
from view.restauranteView import RestauranteView

class RestauranteController:
    def __init__(self):
        self.view = RestauranteView()
        self.gerenciador = GerenciadorRestaurantes()

    def executar(self):
        while True:
            command = self.view.introduction_page()
            if command == 1:
                 self.gerenciador.listar_restaurantes()
            elif command == 2:
                item, preco, descricao = self.view.obter_detalhes_prato()
                self.loja.incluir_prato_no_cardapio(item, preco, descricao)
            elif command == 3:
                item, preco, descricao = self.view.obter_detalhes_bebida()
                self.loja.incluir_bebida_no_cardapio(item, preco, descricao)
            elif command == 4:
                self.loja.listar_cardapio()
            elif command == 5:
                nome, tipo = self.view.obter_detalhes_restaurante()
                self.gerenciador.adicionar_restaurante(nome, tipo) 
            elif command == 6:
                exit()
            else:
                print('\n Comando não encontrado!! \n\n')