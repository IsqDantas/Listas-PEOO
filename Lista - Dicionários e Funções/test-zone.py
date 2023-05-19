from q1 import min_max_dict
from q2 import min_max_dict_values
from q3 import rename_dict_key
from q5 import multiplicar_dict
from q6 import unpack_dict_to_two_lists
from q7 import order_in_dict
from q8 import add_element_to_dict

# Questão 1

cardapio = {
    "Batata frita": 10.00,
    "Cachorro quente": 8.00,
    "Suco de laranja": 5.00
}

min_max = {
    'min': ("Suco de laranja", 5.00),
    'max': ("Batata frita", 10.00)
}

assert min_max_dict(cardapio) == min_max

cardapio_vegano = {
    "Salada de soja": 29.99,
    "Batata frita gourmet": 42.50,
    "Estrogonofe de tofu": 88.30
}

min_max = {
    'min': ("Salada de soja", 29.99),
    'max': ("Estrogonofe de tofu", 88.30)
}

assert min_max_dict(cardapio_vegano) == min_max

# Questão 2

ddd_paises = {
    'Brasil': 55,
    'Estados Unidos': 1,
    'Argentina': 54,
    'Japão': 81
}

assert min_max_dict_values(ddd_paises) == (1, 81)

# Questão 3

cardapio_novo = {
    "Batata frita": 10.00,
    "Cachorro quente": 8.00,
    "Suco de uva": 5.00
}

assert rename_dict_key(cardapio, 'Suco de laranja', 'Suco de uva')

# Questão 5

salarios = {
    'Isaque': 400,
    'Davi': 0,
    'Karolayne': 9999
}

salarios_esperado = {
    'Isaque': -400,
    'Davi': 0,
    'Karolayne': -9999
}

assert multiplicar_dict(salarios, -1) == salarios_esperado

# Questão 6

pessoas = [
    ({'nome': 'Maria',
    'cidade': 'Belo Horizonte'}),

    ({'nome': 'Maria',
    'cidade': 'São Paulo'}),

    ({'nome': 'Pedro',
    'cidade': 'Curitiba'})
]

assert unpack_dict_to_two_lists(pessoas) == (['Maria', 'Maria', 'Pedro'],
                                             ['Belo Horizonte', 'São Paulo', 'Curitiba'])

# Questão 7

salarios = {
    'Isaque': 400,
    'Davi': 0,
    'Karolayne': 99999
}

assert order_in_dict(salarios) == None

salarios = {
    'Davi': -99999,
    'Isaque': 400,
    'Karolayne': 99999
}

assert order_in_dict(salarios) == 'ascendente'

salarios = {
    'Karolayne': 99999,
    'Isaque': 400,
    'Davi': -99999
}

assert order_in_dict(salarios) == 'decrescente'

# Questão 8

assert add_element_to_dict({0: 10, 1: 20}, {2: 30}) == {0: 10, 1: 20, 2: 30}
