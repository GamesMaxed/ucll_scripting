'''
Wanneer studenten iets uploaden via Toledo, dan kunnen
lectoren deze uiteraard weer afhalen. Vervelend is
dat deze inzendingen niet genoemd zijn naar de student,
maar naar hun q-nummer. Stel dat studenten dus
een zip moeten inzenden, dan krijgen lectoren
bestanden met als naam bijvoorbeeld

    submission-q0037313-2017-06-03-11-48-33.zip

Om te weten welke student met welk q-nummer overeenkomt,
krijgen de lectoren per zip ook nog een tekstbestand:

    submission-q0037313-2017-06-03-11-48-33.txt

In dit tekstbestand staat ergens een regel

    Name: Jan De Smet


De bedoeling van deze opgave is dat je, gegeven
een reeks .zip bestanden en bijhorende .txt bestanden,
kan vinden wie welk q-nummer heeft.
Daarna moet je de inhoud van het .zip bestand
extraheren naar een subdirectory met als naam "familienaam-voornaam",
bv. janssens-piet of de-smet-jan. Je mag ervan
uitgaan dat de naam geen spaties bevat, maar de familienaam
kan daarentegen wel spaties bevatten.


Voer eerst het commando

    prepare

uit in de shell. Dit maakt een directory testdata
aan met daaronder .zip en .txt bestanden.
Schrijf een script dat, gegeven een directory,
de .zips en .txts hierin verwerkt en er subdirectories
aanmaakt per inzending.

Om een duidelijker beeld te krijgen van wat
verwacht wordt, kan je de voorbeeldoplossing loslaten op de testdata.

    python solution.py testdata

Verwijder hierna weer de aangemaakte subdirectories.


Het is heel belangrijk dat je ***stapsgewijs*** te werk gaat.
Begin met simpele dingen, en test je code telkens
vooraleer je aan een volgende stap begint.
Je kan bijvoorbeeld als volgt te werk gaan:

1. Namen van alle .txt bestanden afprinten
2. q-nummer halen uit de bestandsnamen en deze afprinten
3. In elk .txt bestand zoeken naar de naam van de student en deze afprinten
4. Namen omzetten van 'Jan Peters' naar 'peters-jan' en deze afprinten
5. Een dictionary opstellen met q-nummers als keys en namen als values, en deze afprinten
etc.

'''
