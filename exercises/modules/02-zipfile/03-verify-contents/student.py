'''
Stel een examen waar studenten hun code moeten inzenden.
De code staat verspreid over meerdere bestanden en er wordt
hen gevraagd om deze bestanden te zippen.
Het doel van de oefening is om een script te schrijven
dat automatisch nagaat of alle gevraagde bestanden in
een zip staan opgenomen.


Stel dat studenten voor het examen drie bestanden a.py, b.py
en c.py moeten inleveren. We maken dan een nieuw bestand expected.txt aan
met als inhoud

    a.py
    b.py
    c.py

Als we dan een reeks inzendingen hebben (d.i. zipbestanden),
dan kunnen we met

    python student.py --expected-files expected.txt x.zip y.zip z.zip

nagaan of alle zips de bestanden a.py, b.py en c.py bevatten.
Het script moet per zipbestand afprinten welke bestanden er ontbreken.


Om te testen of je script werkt, kan je

    prepare

uitvoeren. Dit genereert onder de directory testdata
een reeks bestanden:

    expected.txt
    submission1.zip
    submission2.zip
    submission3.zip

Run je script met

    python student.py --expected-files testdata/expected.txt testdata/*.zip

'''
