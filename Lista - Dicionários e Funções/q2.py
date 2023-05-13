# Não entendi o enunciado dessa questão.
# Vou supor que preciso usar essas funções
# do python em um objeto 'dict_values'

def min_max_dict_values(dicionario: dict) -> tuple:
    valores = dicionario.values()

    return min(valores), max(valores)


def main():
    ddd_paises = {
        'Brasil': 55,
        'Estados Unidos': 1,
        'Argentina': 54,
        'Japão': 81
    }
    print(min_max_dict_values(ddd_paises))


if __name__ == '__main__':
    main()
