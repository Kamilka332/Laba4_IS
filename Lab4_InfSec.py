import re
import random as rnd
from math import gcd


def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def primes(n=1):
    while True:
        if is_prime(n):
            yield n
        n += 1


values = [
    ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з'],
    ['и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р'],
    ['с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'],
    ['ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В'],
    ['Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К'],
    ['Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У'],
    ['Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
    ['Э', 'Ю', 'Я', ' ', '.', ':', '!', '?', ',']
]
P, Y = [], []

pattern = r'[А-я,.:; ]+'
phrase = input('Введите фразу с клавиатуры: ')
while re.fullmatch(pattern, phrase) is None:
    phrase = input('Введенная строка некоректна, повторите ввод: ')

# Step 1
for n in primes():
    if n > 100:
        break
    P.append(n)
while True:
    p, q = rnd.choice(P), rnd.choice(P)
    if p != q and p > 2 and q > 2:
        break
# Step 2
n = p * q
print("n:", n)
# Step 3
f = (p - 1) * (q - 1)
print("f:", f)
# Step 4
for i in range(100):
    if gcd(i, f) == 1 and i != 1:
        e = i
        if e < f:
            break
print("e:", e)
# Step 5
for i in range(f):
    if i * e % f == 1:
        d = i
print("d:", d)
# Step 6
P.clear()
for p in phrase:
    for i in range(len(values)):
        for j in range(len(values[i])):
            if p in values[i][j]:
                P.append(i * len(values[i]) + j + 1)
print(*P)
for i in range(len(P)):
    Y.append(P[i] ** e % n)
print(*Y)

###########################################
#########Обратная операция#################
###########################################

P.clear()
phrase = ''
for i in range(len(Y)):
    P.append(Y[i] ** d % n)
for p in P:
    for i in range(len(values)):
        for j in range(len(values[i])):
            if p == i * len(values[i]) + j + 1:
                phrase += values[i][j]
print('Расшифрованная фраза:', phrase)
