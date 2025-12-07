def wyswietl_parzyste(lista):

    print("Oto parzyste elementy listy:")
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

moja_lista = list(range(1, 11))

wyswietl_parzyste(moja_lista)