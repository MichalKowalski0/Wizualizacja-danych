import sys

# 1. Napisz skrypt, który pobiera od użytkownika zdanie i liczy ilość słów. Użyj funkcji input
def policz_slowa(zdanie):
    slowa = zdanie.split()
    return len(slowa)

# 2. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c. Użyj funkcji readline() i write()).
def dzialanie_na_calkowitych(a, b, c):
    wynik = a**b + c
    return wynik

# 3. Napisz skrypt, który sprawdzi czy wczytany napis jest palindromem.
def czy_palindrom(napis):
    napis = napis.lower().replace(" ", "")
    return napis == napis[::-1]

# 4. Napisz skrypt, który sprawdzi czy wczytana liczba jest pierwsza.
def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

# 5. Napisz skrypt, który sprawdzi ile jest liczb doskonałych do liczby 1000.
def czy_doskonala(liczba):
    suma_dzielnikow = sum(i for i in range(1, liczba) if liczba % i == 0)
    return suma_dzielnikow == liczba

def liczby_doskonale(do_limitu):
    doskonale = [i for i in range(2, do_limitu) if czy_doskonala(i)]
    return doskonale

# 6. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
def podnies_do_kwadratu(lista_liczb):
    wyniki = [liczba**2 for liczba in lista_liczb]
    return wyniki

# 7. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.
def lista_parzystych():
    wyniki = [liczba ** 2 for liczba in lista_liczb]
    return wyniki

# 8. Napisz skrypt, w którym utworzysz listę z elementami dowolnego typu. Utwórz słownik, gdzie klucze będą poszczególnymi elementami z listy, a wartość to ilość wystąpień klucza w liście. Następnie usuń wszystkie elementy ze słownika, które nie będą liczbami.
def stworz_slownik(lista_elementow):
    slownik_wystapien = {}

    for element in lista_elementow:
        if element in slownik_wystapien:
            slownik_wystapien[element] += 1
        else:
            slownik_wystapien[element] = 1

    return slownik_wystapien

def usun_nieliczby(slownik):
    klucze_do_usuniecia = [klucz for klucz in slownik if not isinstance(klucz, (int, float))]
    for klucz in klucze_do_usuniecia:
        del slownik[klucz]

def main():
    zdanie_uzytkownika = input("Podaj zdanie: ")
    ilosc_slow = policz_slowa(zdanie_uzytkownika)
    print(f"Ilość słów w zdaniu to: {ilosc_slow}")

    sys.stdout.write("Podaj trzy liczby całkowite: ")
    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    c = int(sys.stdin.readline().strip())
    wynik_obliczen = dzialanie_na_calkowitych(a, b, c)
    sys.stdout.write(f"Wynik obliczenia {a}^{b} + {c} to: {wynik_obliczen}\n")

    user_input = input("Podaj napis: ")
    if czy_palindrom(user_input):
        print("Podany napis jest palindromem.")
    else:
        print("Podany napis nie jest palindromem.")

    try:
        wczytana_liczba = int(input("Podaj liczbę do sprawdzenia, czy jest pierwsza: "))
        if czy_pierwsza(wczytana_liczba):
            print("Podana liczba jest liczbą pierwszą.")
        else:
            print("Podana liczba nie jest liczbą pierwszą.")
    except ValueError:
        print("Wprowadzono niepoprawne dane. Podaj liczbę całkowitą.")

    limit = 1000
    doskonale_do_1000 = liczby_doskonale(limit)
    print(f"Liczby doskonałe do {limit}: {doskonale_do_1000}")

    lista_liczb = [1, 2.5, 3, 4.2, 5, 6.7, 7, 8.3, 9, 10]
    wyniki_kwadratu = podnies_do_kwadratu(lista_liczb)
    print("Lista przed podniesieniem do kwadratu:", lista_liczb)
    print("Lista po podniesieniu do kwadratu:", wyniki_kwadratu)

    lista_liczb_parzystych = lista_parzystych()
    print("Lista parzystych liczb do kwadratu:", lista_liczb_parzystych)

    lista_elementow = [1, 'a', 2, 'b', 'c', 2, 3, 'a', 4, 'b', 5, 'c', 'd', 'd']
    slownik_wystapien = stworz_slownik(lista_elementow)
    print("Słownik przed usunięciem elementów, które nie są liczbami:", slownik_wystapien)
    usun_nieliczby(slownik_wystapien)
    print("Słownik po usunięciu elementów, które nie są liczbami:", slownik_wystapien)

if __name__ == "__main__":
    main()
