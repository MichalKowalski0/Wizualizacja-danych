import math
import random

def zadanie1():
    wynik1 = round(math.sqrt(3) * (math.exp(4) - math.log(34)), 2)
    wynik2 = round(math.sqrt(3) * (math.log(20) + math.cos(math.radians(45)) + math.e), 2)
    wynik3 = round(math.sqrt(4) * (math.log(20, 3) + math.sin(math.radians(45)) * 5/8), 2)
    wynik4 = round(math.log(23, 3) + math.sqrt(3) * (math.sin(math.radians(34)) + 5), 2)
    wynik5 = round(math.sqrt(4) * (math.log(32, 2) + math.pi + math.sin(math.radians(56))), 2)

    print("Wynik 1:", wynik1)
    print("Wynik 2:", wynik2)
    print("Wynik 3:", wynik3)
    print("Wynik 4:", wynik4)
    print("Wynik 5:", wynik5)

def zadanie2():
    wysokosc = int(input("Podaj wysokość wieży nie większą niż 10: "))
    if wysokosc > 10:
        print("Wysokość wieży nie może przekroczyć 10.")
        return
    for i in range(1, wysokosc + 1):
        print("A" * i)

def zadanie3():
    wysokosc = int(input("Podaj wysokość piramidy nie większą niż 10: "))
    if wysokosc > 10:
        print("Wysokość piramidy nie może przekroczyć 10.")
        return
    for i in range (1, wysokosc + 1):
        spacja = " " * (wysokosc - i)
        litera = "A" * (2 * i - 1)
        print(spacja + litera)

def zapoznanie_funkcja_random():
    # Dodać bliblioteke "random"
    # Generowanie losowej liczby z zakresu [0.0, 1.0)
    losowa_liczba = random.random()
    print("Losowa liczba z zakresu [0.0, 1.0):", losowa_liczba)

    # Generowanie losowej liczby całkowitej z zakresu [1, 10]
    losowa_liczba_calkowita = random.randint(1, 10)
    print("Losowa liczba całkowita z zakresu [1, 10]:", losowa_liczba_calkowita)

    # Losowy wybór elementu z listy
    lista = ['jabłko', 'banan', 'gruszka', 'śliwka', 'mango']
    wylosowany_element = random.choice(lista)
    print("Wylosowany element z listy:", wylosowany_element)

    # Przemieszanie elementów w liście
    random.shuffle(lista)
    print("Przemieszane elementy w liście:", lista)

def zadanie5():
    n = int(input("Podaj wymiary wektora: "))
    wektor = []
    for _ in range(n):
        wiersz = [random.randint(1, 100) for _ in range(n)]
        wektor.append(wiersz)
    sumy_wierszy = [sum(wiersz) for wiersz in wektor]
    print("Sumy elementów z każdego wiersza: ", sumy_wierszy)
    return sumy_wierszy


    wynik = utworz_wektor_i_sumuj()

def main():
    #zadanie1()
    #zadanie2()
    #zadanie3()
    #zapoznanie_funkcja_random()
    #zadanie5()
main()