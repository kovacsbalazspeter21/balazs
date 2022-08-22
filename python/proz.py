lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista1 = max([ szam for szam in lista if szam % 2 == 0])

a = []
for sor in lista:
  if sor % 2 == 0:
    a.append(sor)
print(max(a))



_____________________________________


'''
N�v;Oszt�ly;Els� nap;Utols� nap;Mulasztott �r�k
Balogh P�ter;6a;1;1;5
'''

class Hianyzas:
  def __init__(self, sor):
    nev, osztaly, elso, utolso, mulasztott = sor.strip().split(";")
    self.nev = nev
    self.osztaly = osztaly
    self.elso = int(elso)
    self.utolso = int(utolso)
    self.mulasztott = int(mulasztott)

lista = []
with open("szeptember.csv", encoding="latin2") as f:
  f.readline()
  lista = [Hianyzas(sor) for sor in f]


#2
mulasztasok = sum([sor.mulasztott for sor in lista])
print(mulasztasok)

x = []
for sor in lista:
  x.append(sor.mulasztott)
print(sum(x))
  
#3

szam = int(input("Kérek egy számot 1 és 30 között! "))
nev = input("Kérek egy nevet! ")

if 1 < szam < 30:
  pass
else:
  szam = None

#4

volt_e = [sor.mulasztott for sor in lista if nev == sor.nev and sor.mulasztott > 0]

if len(volt_e):
  print("Hiányzot szeptemberben!")
else:
  print("Nem hiányzot Szeptemberben!")

f = []
for sor in lista:
  if nev == sor.nev and sor.mulasztott > 0:
    f.append(sor.mulasztott)
if len(f) > 0:
  print("Hiányzot szeptemberben!")
else:
  print("Nem hiányzot Szeptemberben!")

#5
hiany = [sor for sor in lista if sor.elso <= szam <= sor.utolso]
[print(f"{sor.nev} ({sor.osztaly})") for sor in hiany]

h = []
for sor in lista:
  if sor.elso <= szam <= sor.utolso:
    h.append(sor.nev, sor.osztaly)


#6
_________________________________________________________________________

