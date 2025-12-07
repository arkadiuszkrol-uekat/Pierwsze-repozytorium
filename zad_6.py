def zlacz_podnies(lista_a: list[int], lista_b: list[int]) -> list:
    combined = list(set(lista_a + lista_b))
    return [x**3 for x in combined]


print(zlacz_podnies([2, 3, 4, 5], [4, 5, 6, 7]))
