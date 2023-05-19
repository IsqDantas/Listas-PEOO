# Não entendi bem o que significa somar
# pessoas, mas vou imaginar que isso
# é unir os elementos de cada dicionário

pessoas = [
    ({'nome': 'Maria',
    'cidade': 'Belo Horizonte'}),

    ({'nome': 'Maria',
    'cidade': 'São Paulo'}),

    ({'nome': 'Pedro',
    'cidade': 'Curitiba'})
]

for i in range(len(pessoas)):
    chave = '-'.join(pessoas[i].keys())
    valor = '-'.join(pessoas[i].values())
    pessoas[i] = {chave: valor}


print(pessoas)
