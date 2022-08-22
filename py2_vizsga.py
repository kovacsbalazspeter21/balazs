# 1. A karakterek_szama(fname) függvény visszatér a fájlban levő karakterek számával. ('\n karakterekkel együtt')
def karakterek_szama(fname):
  with open(fname) as f:
    return len(f.read())                                                 
# 2. A szavak_szama(fname) függvény visszatér a fname) fájlban levő szavak számával.
def szavak_szama(fname):
  with open(fname) as f:
     return len(f.read().split())
        
# 3.  A sorok_szama(fname) függvény visszatér a  fájlban levő sorok számával.   
def sorok_szama(fname):
  with open(fname) as f:
    return len(f.read().split("\n"))
    #return len(f.readlines())
    
      
# 4. Az r_betuk_szama(fname) függvény visszatér a  fájlban levő 'r' betük számával.
def r_betuk_szama(fname):
  with open(fname) as f:
     return f.read().count("r")
    
      
        
# 5. A lorem_szavak_szama(fname) függvény visszatér a  fájlban levő "lorem" szavak számával.
def lorem_szavak_szama(fname):
  with open(fname) as f:
     return f.read().count("lorem")
    
     
    
# 6. A leggyakoribb_karakter(fname) függvény visszatér a  fájlban leggyakrabban előforduló karakterrel.
def leggyakoribb_karakter(fname):
  stat = dict()
  with open(fname) as f:
    for karakter in f.read():
      stat[karakter] = stat.get(karakter, 0) + 1
  return max(stat, key=stat.get)
        
    
    
# 7. A leghosszabb_sor_hossza(fname) függvény visszatér a  fájlban levő leghosszabb sor hosszával.
def leghosszabb_sor_hossza(fname):
  legnagyobb = 0
  with open(fname) as f:
    for sor in f.readlines():
      if len(sor) > legnagyobb:
        legnagyobb = len(sor)
    return legnagyobb
    
    
    
    
    
    
filename = "lorem.txt"
print(f'''
Minta a lorem.txt fájl esetén:
    
1. A karakterek száma: 18047
2. A szavak száma: 2304
3. A sorok száma: 82
4. Az "r" betük száma: 790 
5. A "lorem" szavak száma: 27
6. A leggyakoribb karakter: i 
7. A leghosszabb sor hossza: 304 
-----------------------------------------------------

A program futásának eredménye:

1. A karakterek száma: {karakterek_szama(filename)}
2. A szavak száma: {szavak_szama(filename)}
3. A sorok száma: {sorok_szama(filename)}
4. Az "r" betük száma: {r_betuk_szama(filename)} 
5. A "lorem" szavak száma: {lorem_szavak_szama(filename)}
6. A leggyakoribb karakter: {leggyakoribb_karakter(filename)} 
7. A leghosszabb sor hossza: {leghosszabb_sor_hossza(filename)} 
-----------------------------------------------------   
''')
  