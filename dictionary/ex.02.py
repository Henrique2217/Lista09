pessoa = {
    "nome":"Henrique",
    "email": "htrentin17@gmail.com",
    "idade": "21"
}

print("Chaves em pessoa: ")
for chave in pessoa:
    print(chave)

print("-" * 10)

print("Valores em pessoas: ")
for valor in pessoa.values():
    print(valor)

print("-" * 10)

print("Itens em pessoa: ")
for chave, valor in pessoa.items():
    print(f"Chave:{chave} | Valor: {valor}")