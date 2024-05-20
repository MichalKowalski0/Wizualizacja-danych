import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
def zadanie1():

    x = np.linspace(1, 20, 100)
    y = 1 / x

    plt.plot(x, y, label='f(x) = 1/x')

    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.ylim(0, 1)
    plt.xlim(1, len(x))

    plt.legend()
    plt.show()

def zadanie2():
    def f(x):
        return 1 / x

    x = np.linspace(1, 20, 20)
    plt.plot(x, f(x), 'g:>', label='f(x) = 1/x')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('WYkres funkcji f(x) dla x [1, 20]')
    plt.xlim(0, len(x))
    plt.ylim(0, 1)
    plt.legend()
    plt.show()

def zadanie3():

    x = np.arange(0, 30, 0.1)

    y_sin = np.sin(x)
    y_cos = np.cos(x)

    plt.plot(x, y_sin, label='sin(x)')
    plt.plot(x, y_cos, label='cos(x)')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Wykresy funkcji sin(x) oraz cos(x)')

    plt.legend()
    plt.show()

def zadanie4():

    iris = sns.load_dataset('iris')

    x = iris['sepal_length']
    y = iris['sepal_width']

    palette = sns.color_palette("viridis", as_cmap=True)

    s = np.abs(x - y) * 100

    plt.scatter(x, y, c=y, s=s, cmap=palette, alpha=0.6, edgecolors="w", linewidth=0.5)


    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')

    plt.title('Wykres punktowy Sepal Length vs Sepal Width')

    plt.colorbar(label='Sepal Width')

    plt.show()


def main():
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()

main()