import numpy as np

# wczytanie danych od użytkownika
n = int(input("Podaj wartość n: "))
x = np.zeros(n)
y = np.zeros(n)

for i in range (n):
    x[i] = input(f"Podaj x[{i+1}]: ")
    y[i] = input(f"Podaj y[{i+1}]: ")

# właściwa realizacja algorytmu
s1 = 0
s2 = 0
s3 = 0
s4 = 0

for i in range (n):
    s1 = s1 + x[i]
    s2 = s2 + y[i]
    s3 = s3 + (x[i] * x[i])
    s4 = s4 + (x[i] * y[i])

w = (n * s3) - (s1 * s1)
w1 = (s2 * s3) - (s4 * s1)
w2 = (n * s4) - (s1 * s2)

p0 = w1/w
p1 = w2/w

print(f"x: {x}")
print(f"y: {y}")

# wyświetlenie wyników
print(f"Wartość p0 wynosi: {p0}")
print(f"Wartość p1 wynosi: {p1}")
