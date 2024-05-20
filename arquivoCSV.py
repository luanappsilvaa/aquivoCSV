# Solicita ao usuário que insira seu nome, idade e cidade
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

# Cria um dicionário para armazenar as informações
pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

# Cria uma lista e adiciona o dicionário a ela
lista_pessoas = []
lista_pessoas.append(pessoa)

# Exibe as informações armazenadas na lista
print("\nLista de Pessoas:")
for pessoa in lista_pessoas:
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("Cidade:", pessoa["cidade"])
    print()  # Adiciona uma linha em branco entre as pessoas
