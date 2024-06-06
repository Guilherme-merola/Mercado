from time import sleep
from produtos import *
from typing import List, Dict


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def menu() -> None:
    print("-----------------------------------------")
    print("------- Seja bem-vindo ao mercado -------")
    print("-----------------------------------------\n")
    print("---- Selecione uma das opções abaixo ----")
    print("""
-----------------------------------------
1- Cadastrar produtos
2- Listar produtos
3- Adicionar produto no carrinho
4- Listar produtos no carrinho
5- Finalizar pedido
6- Sair
-----------------------------------------
""")
    opcao = input()
    print("")

    if opcao == '1':
        cadastrar_produtos()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        adicionar_carrinho()
    elif opcao == '4':
        listar_carrinho()
    elif opcao == '5':
        finalizar_pedido()
    elif opcao == '6':
        sair()
    else:
        print("Opção inválida")
        sleep(2)
        menu()


def cadastrar_produtos() -> None:
    print("------------------------------------------")
    print("---------- Cadastro de produtos ----------")
    print("------------------------------------------\n")

    try:
        nome = input("Digite o nome do produto  ")
        preco = float(input("Digite o preço do produto  "))
        produtos.append(Produto(nome, preco))
        print("\nProduto cadastrado com sucesso!")
        
    except:
        print("Ocorreu algum erro, tente novamente")

    print("")
    sleep(2)
    menu()



def listar_produtos() -> None:
    if len(produtos) > 0:
        print("------------------------------------------")
        print("---------- Produtos cadastrados ----------")
        print("------------------------------------------")

        for items in produtos:
            print(items)
            sleep(1)
    else:
        print("Não há produtos cadastrados")

    print("")
    sleep(2)
    menu()


def adicionar_carrinho() -> None:
    if len(produtos) > 0:
        print("-------------------------------------------")
        print("------- Informe o código do produto -------")
        print("-------------------------------------------")

        for produto in produtos:
            print(produto)
            sleep(1)

        codigo: int = int(input())
        produto = varrendo_produtos(codigo)

        if produto:
            print("\nInforme a quantidade que deseja adicionar")
            quantidade: int = int(input())
            print("")

            if len(carrinho) > 0:
                produto_carrinho: bool = False
                for item in carrinho:
                    quantidade_carrinho: int = item.get(produto)
                    
                    if quantidade_carrinho:
                        print(f"O {produto.nome} ja está no carrinho, deseja adionar mais unidades? (Sim/Não)")
                        opcao: str = input().lower()
                        print("")

                        if opcao == 'sim':
                            item[produto] = quantidade + quantidade_carrinho
                            print(f"Foram adicionadas {quantidade} unidades de {produto.nome} no carrinho com sucesso!")
                            produto_carrinho = True
                            
                        else:
                            print("Não foram feitas alterações no carrinho")

                if not produto_carrinho:
                    carrinho.append({produto: quantidade})
                    print(f"{quantidade} unidades do {produto.nome} foram adicionadas com sucesso!")

            else:
                carrinho.append({produto: quantidade})
                print(f"{quantidade} unidades do {produto.nome} foram adicionadas com sucesso!")

        else:
            print("Não existe esse produto cadastrado")
            sleep(2)
            adicionar_carrinho()

    else:
        print("Não há produtos cadastrados")

    print("")
    sleep(2)
    menu()


def listar_carrinho() -> None:
    if len(carrinho) > 0:
        print("------------------------------------------")
        print("---------- Produtos no carrinho ----------")
        print("------------------------------------------")

        for items in carrinho:
            for dados in items.items():
                print(f"{dados[-1]} unidades de {dados[0].nome}")
                sleep(1)

    else:
        print("Não há produtos no carrinho")

    print("")
    sleep(2)
    menu()

def finalizar_pedido() -> None:
    if len(carrinho) > 0:  
        print("------------------------------------------")
        print("------------ Finalizar pedido ------------")
        print("------------------------------------------")
        valor_total: float = 0

        for items in carrinho:
            for dados in items.items():
                print(f"{dados[-1]} unidades de {dados[0].nome} = {conversor_float_str(dados[0].somar_valor(dados[-1]))}")
                valor_total += dados[0].somar_valor(dados[-1])

        print(f"\nValor total da compra: {conversor_float_str(valor_total)}")
        carrinho.clear()
        
    else:
        print("Não foram adicionados produtos ao carinho")

    print("")
    sleep(2)
    menu()


def sair() -> None:
    print("Volte sempre")
    sleep(3)
    exit(0)


def varrendo_produtos(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo_produto == codigo:
            p = produto

    return p


if __name__ == '__main__':
    menu()