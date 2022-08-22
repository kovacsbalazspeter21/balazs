""" 
#--------------------------------------------------------
# 7. Melyik ország csatlakozott utoljára?
def utoljara_csatlakozott_orszag(lista):
  szamlalo = ""
  orszag = ""
  for sor in lista:
    if sor.datum > szamlalo:
      szamlalo = sor.datum
      orszag = sor.orszag
  return orszag
    
    
      
print(
    f"7. Utoljára csatlakozott ország neve: {utoljara_csatlakozott_orszag(lista)} "
)
#--------------------------------------------------------


# 8. Mely hónapban csatlakozott a legtöbb ország? (Bemenő paraméter az adatokat tartalmazó lista, visszatérési érték a hónap integer típusként.)
def legtobb_csatlakozas_honapja(lista):
   stat = dict()

   for sor in lista:
     stat[sor.honap] = stat.get(sor.honap, 0) + 1
   return max(stat, key=stat.get)
    
    
    
print(
    f"8. A legtöbb ország a következő hónapban csatlakozott: {legtobb_csatlakozas_honapja(lista)}"
)
#--------------------------------------------------------


# 9. A megadott évben hány tagállama volt az Eu-nak?
def tagallamok_szama_az_adott_evben(lista, ev):
  tagok =  0
  for sor in lista:
    if sor.ev <= ev:
      tagok += 1
  return tagok
    
    
      
print(
    f"9. A tagállamok száma 2000-ben: {tagallamok_szama_az_adott_evben(lista, 2000)}"
)
print(f'''
Minta:
1. Osztály létrehozása Eu: néven
2. A 'csatlakozas.txt' fájl beolvasása, a lista létrehozása.
3. A tagállamok száma 2018-ban: 28
4. Csatlakozások száma 2007-ben: 2 
5. Csatlakozások száma májusban: 10 
6. Magyarország csatlakozási dátuma: 2004.05.01
7. Utoljára csatlakozott ország neve: Horvátország 
8. A legtöbb ország a következő hónapban csatlakozott: 1
9. A tagállamok száma 2000-ben: 15
''')
