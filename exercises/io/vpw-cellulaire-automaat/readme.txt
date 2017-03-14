Voer uit op de console:

     prepare


Dit downloadt een aantal bestanden, waaronder opgave.pdf waarin
de opdracht beschreven staat.

Doe eerst de tests slagen door de nodige functies te implementeren.
Vervolgens kan je je algoritme toepassen op echte IO van de VPW.
Dit doe je door de invoer (beschreven in opdracht.pdf) in te lezen
met input() en de uitvoer uit te schrijven d.m.v. print.
Om te testen of het lukt, run je je script vanop de console:

   cat voorbeeld.invoer | python student.py | diff - voorbeeld.uitvoer

Dit voedt voorbeeld.invoer aan je script, en diff vergelijkt
daarna de uitvoer van je script met voorbeeld.uitvoer.
Indien diff niets afprint, betekent dat je alles juist hebt.
Hierna kan je het tevens uittesten op de wedstrijdinvoer:

   cat wedstrijd.invoer | python student.py | diff - wedstrijd.uitvoer

