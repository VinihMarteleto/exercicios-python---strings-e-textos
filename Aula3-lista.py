# Exemplo de listas em Python
Vendas = [100, 200, 300, 400, 500]
print(Vendas[-1])  # Acessa o último elemento da lista

qtde_vendas = len(Vendas)
print(qtde_vendas)  # Imprime o tamanho da lista

#soma dos elementos da lista
total_vendas = sum(Vendas)
print(total_vendas)

#valor maximo e minimo
print(max(Vendas))
print(min(Vendas))
print(total_vendas / len(Vendas))  # média das vendas

#encontrar um elemento na lista

lista_produtos = ["camiseta", "calça", "tênis", "bermuda"]
print("calça" in lista_produtos)  # Verifica se "calça" está na lista
posicao = lista_produtos.index("calça")
print(posicao)  # Imprime a posição de "calça" na lista

pedaço_lista = lista_produtos[posicao:]
print(pedaço_lista)  # Imprime o pedaço da lista a partir de "calça"

# editar um elemento da lista
lista_valor = [5000, 15000, 25000, 35000]
novo_valor = lista_valor[1] * 1.1  # Aumenta o primeiro valor em 10%
lista_valor[1] = novo_valor
print(lista_valor)  # Imprime a lista atualizada

#remover um elemento da lista
lista_produtos.remove("tênis")  # Remove o elemento na posição 2
print(lista_produtos)  # Imprime a lista após a remoção

#adicionar um elemento na lista
lista_produtos.append("meia")
print(lista_produtos)  # Imprime a lista após a adição

lista2_produtos = ["boné", "óculos"]\
    + lista_produtos  # Concatena duas listas
print(lista2_produtos)  # Imprime a lista concatenada

#inserir um elemento na lista em uma posição específica
lista2_produtos.insert(2, "carteira")
print(lista2_produtos)

# contando elementos na lista
lista2_produtos.count("óculos")
print(lista2_produtos.count("óculos"))  # Imprime a contagem de "óculos" na lista

#ordenando uma lista
lista2_produtos.sort(reverse=False)  # Ordena a lista em ordem crescente
print(lista2_produtos)  # Imprime a lista ordenada