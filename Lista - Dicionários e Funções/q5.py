def multiplicar_dict(dicionario: dict, fator: float):
    for chave, valor in dicionario.items():
        dicionario[chave] = valor * fator
    
    return dicionario


def main():
    salarios = {
        'Isaque': 400,
        'Davi': 0,
        'Karolayne': 9999
    }

    print(multiplicar_dict(salarios, -1))


if __name__ == '__main__':
    main()
