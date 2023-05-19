def add_element_to_dict(dicionario: dict, elemento: dict) -> dict:
    dicionario.update(elemento)
    return dicionario


def main():
    assert add_element_to_dict({0: 10, 1: 20}, {2: 30}) == {0: 10, 1: 20, 2: 30}


if __name__ == '__main__':
    main()
