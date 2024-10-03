

#tupla
campos = ("nome","idade","profisao","E-mail")

#dicionario
usuario = {}

#entrada de dados
for campo in campos:
    usuario[campo]= input(f"informe o valor do campo{campo}:")



#exibir os valores de dicionario na tela
print("DADOS DO USUARIO:\n")
for campo in campos:
    print(f"{campo}:{usuario.get(campo)}.")
