def czy_pierwsze_dwie_wieksze(liczba_1: int, liczba_2: int, liczba_3: int) -> bool:
    if liczba_1+liczba_2>liczba_3:
        return True
    else:
        return False
    
print(czy_pierwsze_dwie_wieksze(4,3,6))