def czy_zawiera(lista: list, liczba:int)-> bool:
    for element in lista:
        if liczba==element:
            return True
    return False

print(czy_zawiera([2,3,4],5))