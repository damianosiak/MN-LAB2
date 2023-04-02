import numpy as np
import matplotlib.pyplot as plt

# ----- WCZYTANIE DANYCH OD UŻYTKOWNIKA -----
n = int(input("Podaj wartość n: "))

x = np.zeros(n)
y = np.zeros(n)

for i in range (n):
    x[i] = input(f"Podaj x[{i+1}]: ")
    y[i] = input(f"Podaj y[{i+1}]: ")


# ----- UZUPEŁNIENIE TABLIC -----
lnx = np.zeros(n)
lnx2 = np.zeros(n)
ylnx = np.zeros(n)

for i in range (n):
    lnx[i] = np.log(x[i])
    lnx2[i] = lnx[i] * lnx[i]
    ylnx[i] = y[i] * lnx[i]


# ----- SUMOWANIE -----
sum_y = 0
sum_lnx = 0
sum_lnx2 = 0
sum_ylnx = 0

for i in range (n):
    sum_y += y[i]
    sum_lnx += lnx[i]
    sum_lnx2 += lnx2[i]
    sum_ylnx += ylnx[i]


# ----- UKŁAD RÓWNAŃ -----
# { (sum_lnx2 * a) + (sum_lnx * b) = sum_ylnx
# { (sum_lnx * a) + (n * b) = sum_y


# ----- ROZWIĄZANIE UKŁADU RÓWNAŃ (PRZEKSZTAŁCONE NA POSTAĆ ax + by = c) -----
# a1, b1, c1
# a2, b2, c2
a1 = sum_lnx2
b1 = sum_lnx
c1 = sum_ylnx
a2 = sum_lnx
b2 = n
c2 = sum_y

# ----- WYKORZYSTANIE WSPÓŁCZYNNIKA DLA METODY ELIMINACJI GAUSSA -----
m = a2/a1
a2 -= m*a1
b2 -= m*b1
c2 -= m*c1

# ----- OBLICZENIE WARTOŚCI NIEWIADOMYCH A i B -----
B = c2/b2
A = (c1 - b1*B)/a1

# ----- WYPISANIE WZORU FUNKCJI y -----
print(f"y = {A} lnx + {B}")

# ------ OBLICZENIE yobl DLA WPROWADZONYCH PUNKTÓW x -----
yobl = np.zeros(n)
for i in range (n):
    yobl[i] = (A * lnx[i]) + B

# ----- GENEROWANIE DODATKOWYCH PUNKTÓW POMIĘDZY PUNKTEM x=0 A OSTATNIM ELEMENTEM TABLICY PUNKTÓW x, OBLICZENIE DLA TYCH PUNKTÓW WARTOŚCI yobl_new -----
x_new = np.linspace(0, max(x), 1000)
yobl_new = A * np.log(x_new) + B

# ----- RYSOWANIE WYKRESU -----
plt.plot(x, yobl, 'bo',label="yobl")
plt.plot(x_new, yobl_new,'r',label="")
plt.xlabel('x')
plt.ylabel('y')
plt.title("MN-LAB2: Realizacja y = a*ln(x) + b")
plt.legend()
plt.show()

print(f"x: {x}")
print(f"y: {y}")
print(f"yobl: {yobl}")
