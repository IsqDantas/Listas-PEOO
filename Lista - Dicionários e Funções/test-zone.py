from q1 import min_max_dict
from q2 import min_max_dict_values
from q3 import rename_dict_key

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
