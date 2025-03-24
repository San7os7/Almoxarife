# Dicionário para armazenar os produtos e quantidades
estoque = {
    "Parafuso": 50,
    "Prego": 100,
    "Martelo": 10
}

def exibir_estoque():
    """Exibe o estoque atual"""
    print("\n📦 Estoque Atual:")
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade} unidades")
    print("-" * 30)

def entrada_estoque():
    """Adiciona produtos ao estoque"""
    produto = input("Digite o nome do produto para entrada: ").capitalize()
    quantidade = int(input("Quantidade a adicionar: "))

    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade
    
    print(f"✅ {quantidade} unidades de {produto} adicionadas ao estoque!")

def saida_estoque():
    """Remove produtos do estoque"""
    produto = input("Digite o nome do produto para saída: ").capitalize()
    
    if produto in estoque:
        quantidade = int(input(f"Quantidade de {produto} a remover: "))
        
        if quantidade > estoque[produto]:
            print("❌ Erro: Quantidade insuficiente no estoque!")
        else:
            estoque[produto] -= quantidade
            print(f"✅ {quantidade} unidades de {produto} retiradas do estoque!")
            
            # Se a quantidade chegar a zero, remover o produto do estoque
            if estoque[produto] == 0:
                del estoque[produto]
                print(f"⚠️ {produto} esgotou e foi removido do estoque.")
    else:
        print("❌ Produto não encontrado no estoque!")

# Menu principal
while True:
    print("\n🔹 Escolha uma opção:")
    print("1️⃣ Entrada de produtos")
    print("2️⃣ Saída de produtos")
    print("3️⃣ Exibir estoque")
    print("4️⃣ Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        entrada_estoque()
    elif opcao == "2":
        saida_estoque()
    elif opcao == "3":
        exibir_estoque()
    elif opcao == "4":
        print("🚪 Saindo do sistema...")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")
