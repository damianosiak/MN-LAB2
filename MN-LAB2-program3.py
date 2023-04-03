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
lny = np.zeros(n) #lny
x2 = np.zeros(n) #x2
xlny = np.zeros(n)  #xlny

for i in range (n):
    lny[i] = np.log(y[i])
    x2[i] = x[i] * x[i]
    xlny[i] = x[i] * lny[i]


# ----- SUMOWANIE -----
sum_x = 0
sum_lny = 0
sum_x2 = 0
sum_xlny = 0

for i in range (n):
    sum_x += x[i]
    sum_lny += lny[i]
    sum_x2 += x2[i]
    sum_xlny += xlny[i]

# ----- ROZWIĄZANIE UKŁADU RÓWNAŃ (PRZEKSZTAŁCONE NA POSTAĆ ax + by = c) -----
# a1, b1, c1
# a2, b2, c2
a1 = n
b1 = sum_x
c1 = sum_lny
a2 = sum_x
b2 = sum_x2
c2 = sum_xlny

# ----- WYKORZYSTANIE WSPÓŁCZYNNIKA DLA METODY ELIMINACJI GAUSSA -----
m = a2/a1
a2 -= m*a1
b2 -= m*b1
c2 -= m*c1

# ----- OBLICZENIE WARTOŚCI NIEWIADOMYCH A i B, a następnie aa -----
B = c2/b2
A = (c1 - b1*B)/a1
aa = np.exp(A)

# ----- WYPISANIE WZORU FUNKCJI y -----
print(f"y = {aa} exp({B}x)")

# ------ OBLICZENIE yobl DLA WPROWADZONYCH PUNKTÓW x -----
yobl = np.zeros(n)
for i in range (n):
    yobl[i] = aa * np.exp(B * x[i])

# ----- GENEROWANIE DODATKOWYCH PUNKTÓW POMIĘDZY PUNKTEM x=0 A OSTATNIM ELEMENTEM TABLICY PUNKTÓW x, OBLICZENIE DLA TYCH PUNKTÓW WARTOŚCI yobl_new -----
x_new = np.linspace(0, max(x), 1000)
yobl_new = aa * np.exp(B * x_new)

# ----- RYSOWANIE WYKRESU -----
plt.plot(x, yobl, 'bo',label="yobl")
plt.plot(x_new, yobl_new,'r',label="")
plt.xlabel('x')
plt.ylabel('y')
plt.title("MN-LAB2: Realizacja y = a*exp(bx)")
plt.legend()
plt.show()

print(f"x: {x}")
print(f"y: {y}")
print(f"yobl: {yobl}")
