'''
800 600 100
38522 Aradi 1 C 180
'''
class Project():
    def __init__(self, sor):
        tulajdonos_adoszam, utca_neve, utca_szam, adoszam, negyzet_terulet = sor.strip().split(" ")
        self.tulajdonos_adoszam = tulajdonos_adoszam
        self.utca_neve = utca_neve
        self.utca_szam = utca_szam
        self.adoszam = adoszam
        self.negyzet_terulet = negyzet_terulet
        
with open("utca.txt", "r", encoding="UTF-8") as f:
    cim_sor = f.readline()
    lista = [Project(sor) for sor in f]

#3. Feladat
adoszam_beker = print(int(input("Kérem az adószámot írja be!! ")))
for sor in lista:
  if adoszam_beker == sor.tulajdonos_adoszam:
    print(f"4. Feladat: {sor}")

#4. Feladat
def ado():
  for sor in lista:
    if 600 > sor.negyzet_terulet >= 100:
      print("A")
    elif 800 > sor.negyzet_terulet >= 600:
      print("B")
    elif 800 <= sor.negyzet_terulet:
      print("C")
    return ado(sor)
