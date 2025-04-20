produtos = {
    1: {"nome": "Camisa", "preco": 50.0},
    2: {"nome": "Calça", "preco": 80.0},
    3: {"nome": "Tênis", "preco": 120.0}
}

carrinho = []

def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for codigo, info in produtos.items():
        print(f"{codigo}: {info['nome']} - R${info['preco']:.2f}")

def adicionar_ao_carrinho(codigo):
    if codigo in produtos:
        carrinho.append(produtos[codigo])
        print(f"{produtos[codigo]['nome']} adicionado ao carrinho.")
    else:
        print("Código inválido.")

def ver_carrinho():
    print("\nSeu carrinho:")
    total = 0
    for item in carrinho:
        print(f"- {item['nome']} - R${item['preco']:.2f}")
        total += item['preco']
    print(f"Total: R${total:.2f}")

# Simulador
while True:
    print("\n1 - Ver produtos")
    print("2 - Adicionar produto ao carrinho")
    print("3 - Ver carrinho")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        mostrar_produtos()
    elif escolha == "2":
        try:
            codigo = int(input("Digite o código do produto: "))
            adicionar_ao_carrinho(codigo)
        except ValueError:
            print("Por favor, digite um número válido.")
    elif escolha == "3":
        ver_carrinho()
    elif escolha == "4":
        print("Obrigado por visitar nossa loja!")
        break
    else:
        print("Opção inválida.")
