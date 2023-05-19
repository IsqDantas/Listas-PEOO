# Há três possibilidades nesse caso: o dicionário
# pode estar ordenado - e, então, crescentemente
# ou decrescentemente - ou não ordenado.

def order_in_dict(dicionario: dict):
    valores = list(dicionario.values())
    valores.sort(reverse=False)
    ascendente = valores
    
    valores = list(dicionario.values())
    valores.sort(reverse=True)
    decrescente = valores

    valores = list(dicionario.values())

    if valores == ascendente:
        return 'ascendente'
    elif valores == decrescente:
        return 'decrescente'
    else:
        return None


def main():
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


if __name__ == '__main__':
    main()
