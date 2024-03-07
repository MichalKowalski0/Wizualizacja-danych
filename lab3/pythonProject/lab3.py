#try:
#    a = int(input())
#    b = int(input())
#    result = a / b
#    print(result)
#except ZeroDivisionError:
#    print("Error")
#except ValueError:
#    print("brak liczby")
#import math
import math

#a = [x**2 for x in range(10)]
#print(a)
#l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#l2 = []
#for i in l1:
#    l2.append(i**2)
#print(l2)
#b = [3**y for y in range(6)]
#print(b)
#c = [x for x in a if x % 2 ==1]
#print(c)
#d = [(i, j) for i in l1 for j in l2]

#l3 = []
#for i in l1:
#    for j in l2:
#        l3.append(i,j)
#print(l3)

#s1 = {1:2, 2:3, 3:4}
#s2 = {v: k for k, v in s1.items()}
#print(s2)

#def rownanie_kwadratowe(a, b, c):
 #   delta = b**2 - 4*a*c
 #   if delta <0:
 #       print("brak rozwiazan")
 #       return x
 #   elif delta > 0:
 #       x1 = (-b + math.sqrt(delta))/(2*a)
 #       x2 = (-b - math.sqrt(delta))/(2*a)
 #       print("dwa rozwiazania")
 #       return (x1,x2)

#print(rownanie_kwadratowe(6, 1, 3))
#print(rownanie_kwadratowe(1, 2, 1))
#print(rownanie_kwadratowe(1, 4, 1))

# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)
#
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(2, 4, 5, 7))
# print(dlugosc_odcinka(1, 2, 3, 4))
# print(dlugosc_odcinka(2, 3, 7, 8))

# plik = open('tekst.txt', 'r', encoding='utf8')
# znaki = plik.read(10)
# linia = plik.read()
# linie = plik.readlines()
# plik.close()
#
# print(znaki)
# print(linia)
# print(linie)

# plik = open('plik.txt', 'a+', encoding='utf-8')
# plik = open('plik.txt', 'w', encoding='utf-8')
# plik.seek(0)
# znaki = plik.read(10)
# plik.write('aaadq')
# plik.close()
# print(znaki)

# with open('tekst.txt', 'r') as plik:
#     znaki = plik.readlines()
#
# print(znaki)

import math
import random

# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
def zadanie1():
    A = {(1 - x, x) for x in range(1, 11)}
    B = {2 ** i for i in range(0, 6)}
    C = {x for x in B if x % 2 == 0}
    print("Zbiór A:", A)
    print("Zbiór B:", B)
    print("Zbiór C:", C)

#Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj nową listę, która będzie zawierała tylko parzyste elementy
def zadanie2():
    lista1 = [random.randint(1, 100) for _ in range(10)]
    lista_parzysta = [liczba for liczba in lista1 if liczba % 2 == 0]
    print("Wygenerowana lista:", lista1)
    print("Nowa lista zawierająca tylko parzyste elementy:", lista_parzysta)

#Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
def zadanie3():
    produkty_spozywcze = {
        'jajka': 'sztuki',
        'mleko': 'litr',
        'chleb': 'sztuki',
        'pomidory': 'kg',
        'ser': 'gramy',
        'jogurt': 'sztuki',
        'cukier': 'kg',
        'ziemniaki': 'kg',
        'woda': 'litry',
        'kawa': 'gramy'
    }

    produkty_sztuki = {produkt: jednostka for produkt, jednostka in produkty_spozywcze.items() if jednostka.lower() == 'sztuki'}
    print("Słownik produktów spożywczych:", produkty_spozywcze)
    print("Lista produktów, których wartość to 'sztuki':", produkty_sztuki)

#Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
def zadanie4():
    def czy_trojkat_prostokatny(a, b, c):
        sorted_boki = sorted([a, b, c])
        if sorted_boki[0] ** 2 + sorted_boki[1] ** 2 == sorted_boki[2] ** 2:
            return True
        else:
            return False

    a = 3
    b = 4
    c = 5

    if czy_trojkat_prostokatny(a, b, c):
        print("Trójkąt o bokach {}, {} i {} jest prostokątny.".format(a, b, c))
    else:
        print("Trójkąt o bokach {}, {} i {} nie jest prostokątny.".format(a, b, c))

#Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
def zadanie5(a=1, b=2, h=3):
    pole = 0.5 * (a + b) * h
    print("Pole trapezu (z wartościami domyślnymi):", pole)

#Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
def zadanie6(a1=1, b=4, ile=10):
    wynik = 1
    aktualny_element = a1
    for _ in range(ile):
        wynik *= aktualny_element
        aktualny_element *= b
    print("Iloczyn elementów ciągu:", wynik)

#Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.
def zadanie7():
    try:
        liczba = float(input("Podaj liczbę: "))
        if liczba < 0:
            raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej.")
        pierwiastek = math.sqrt(liczba)
        print(f"Pierwiastek z {liczba} to {pierwiastek}")
    except ValueError as e:
        print(f"Błąd: {e}")

def main():
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
    zadanie5()
    zadanie6()
    zadanie7()

main()






