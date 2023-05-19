def unpack_dict_to_two_lists(dicionarios: list):
    chaves = list(dicionarios[0].keys())

    valores_1 = list()
    valores_2 = list()

    for dicionario in dicionarios:
        valores_1.append(dicionario[chaves[0]])
        valores_2.append(dicionario[chaves[1]])

    return valores_1, valores_2


def main():
    pessoas = [
        ({'nome': 'Maria',
        'cidade': 'Belo Horizonte'}),

        ({'nome': 'Maria',
        'cidade': 'São Paulo'}),

        ({'nome': 'Pedro',
        'cidade': 'Curitiba'})
    ]

    nome, cidade = unpack_dict_to_two_lists(pessoas)

    assert nome == ['Maria', 'Maria', 'Pedro']
    assert cidade == ['Belo Horizonte', 'São Paulo', 'Curitiba']


if __name__ == '__main__':
    main()
