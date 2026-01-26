faturamento = 1000
custo = 600

lucro = faturamento - custo
texto = f"o lucro foi de R${lucro} e o faturamento foi de R${faturamento}"
print(texto)

email = " EMAIL_FALSO@gmail.com "

email = email.lower() #colocar em letra minuscula
email = email.strip() #ajustar esspaços vazios
print(email)

#tamanho 
print(len(email))

#posiçao
posicao = email.find("@")
print(posicao)

#pedaços do texto
print(email[posicao:])

#troca um pedaco do texto
novo_email = email.replace("gmail.com", "yahoo.com.br")
print(novo_email)


nome = "vinicius marteleto"
nome = nome.capitalize()
print(nome)
nome = nome.title()
print(nome)
nome = nome.upper()
print(nome)

#formaçao numerica
faturamento = 1000
custo = 600

lucro = faturamento - custo
margem = lucro / faturamento
texto = f"o lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento:,.2f} e a margem foi de {margem:.1%}"
print(texto)

#exercicio
nome = "vinicius marteleto"
email = "vinihmarteleto@gmail.com"

posicao = email.find("@")
servidor = email[:posicao]
print(servidor)

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
primeiro_nome = primeiro_nome.title()
print(primeiro_nome)

#mensagem de texto 

mensagem = f"Usuario {primeiro_nome} foi cadastrado com sucesso no email {email}"
print(mensagem)