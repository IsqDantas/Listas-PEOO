def rename_dict_key(dictionary: dict, key_to_rename, new_name) -> dict:
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    index_key_to_rename = keys.index(key_to_rename)
    keys[index_key_to_rename] = new_name

    dictionary = {key: value for key, value in zip(keys, values)}

    return dictionary


def main():
    cardapio = {
        "Batata frita": 10.00,
        "Cachorro quente": 8.00,
        "Suco de laranja": 5.00
    }

    print(rename_dict_key(cardapio, 'Suco de laranja', 'Suco de uva'))


if __name__ == '__main__':
    main()
