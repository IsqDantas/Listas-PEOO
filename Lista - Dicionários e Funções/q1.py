def min_max_dict(dicionario: dict) -> dict:
    valores = list(dicionario.values())
    items = list(dicionario.items())

    indice_max = valores.index(max(valores))
    indice_min = valores.index(min(valores))

    max_item = items[indice_max]
    min_item = items[indice_min]

    return {'min': min_item, 'max': max_item}


def main():
    cardapio = {
        "Batata frita": 10.00,
        "Cachorro quente": 8.00,
        "Suco de laranja": 5.00
    }

    print(min_max_dict(cardapio))


if __name__ == '__main__':
    main()
