tree(path) moet de directorystructuur op path visualiseren.
Om de functie te testen, is er een dummy directorystructuur
meegeleverd. Deze vind je onder 'testdir'.

path('testdir') moet als resultaat de volgende string opleveren:

[foo]
  bar.txt
  foo.txt
foo.txt
[qux]
  aaa.txt
  [bar]
    a.txt
    b.txt
  bbb.txt
  ccc.txt


path('testdir/qux') moet opleveren

aaa.txt
[bar]
  a.txt
  b.txt
bbb.txt
ccc.txt


Regels:
- Directories moeten tussen [ ] staan.
- Entries binnen een directory moeten geïndenteerd worden met 2 spaties
- Op elk niveau moeten de bestanden en directories alfabetisch gesorteerd staan
- Het resultaat moet een enkele string zijn die alle lijnen bevat
- Lijnen worden gescheiden door een newline "\n"
