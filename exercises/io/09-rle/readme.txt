RLE is een eenvoudig compressiealgoritme
dat gebruikt wordt in bepaalde grafische
bestandsformaten en faxmachines.
Voor deze opgave moet je een licht
vereenvoudigde versie van dit algoritme
implementeren.

RLE gaat ervan uit dat het bestand
lange reeksen dezelfde tekens bevat, bv.

      aaaabbbbbbbbbbc

Dit wordt omgevormd tot

    4a10b1c

Met andere woorden, RLE telt het aantal
voorkomens van een teken en vervangt de reeks
door dit aantal gevolgd door het teken.


Doe eerst de tests slagen door
de nodige functies te implementeren.
Zorg er hierna voor dat je je
script ook vanop de command line kunt
opstarten als volgt:

    cat testdata/plaintext.txt | python student.py compress

moet de RLE compressie afprinten van de gegeven invoer afprinten.

    cat testdata/compressed.txt | python student.py decompress

moet de inhoud van compressed.txt dan weer decomprimeren.
M.a.w., een command line argument moet je script duidelijk
maken of je wenst te comprimeren of te decomprimeren.


Als na te gaan of de (decompressie) lukt, kun je de output
van je script laten vergelijken door diff:

    cat testdata/plaintext.txt | python student.py compress | diff - testdata/compressed.txt
    cat testdata/compressed.txt | python student.py decompress | diff - testdata/plaintext.txt

Indien alles ok is, zou het uitvoeren van deze twee opdrachten
niets moeten afprinten, wat erop wijst dat er geen verschil is
tussen de door je script geproduceerde uitvoer en de verwachte uitvoer.
