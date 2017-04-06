'''
Schrijf een Python script dat, gegeven een lijst van zips,
afprint hoeveel bestanden er in elk van deze zips zitten.

Om je script te testen, voer je eerst

  prepare

uit in de shell. Dit maakt een aantal zips aan in een subdirectory testdata.
Als je dan bijvoorbeeld

  python solution.py testdata/test1.zip testdata/test2.zip testdata/test3.zip

uitvoert, wordt hetvolgende afgeprint:

  testdata/test1.zip 5
  testdata/test2.zip 11
  testdata/test3.zip 29

Als je zelf gaat kijken in deze zips, zal je
zien dat deze inderdaad 5, 11 en 29 bestanden, respectivelijk, bevatten.


Je hoeft de zips niet expliciet op te sommen:

  python solution.py testdata/*

De shell zal zelf testdata/* vervangen door alle bestanden
die het kan vinden onder testdata, waardoor je script
opgeroepen wordt met [ 'testdata/test1.zip', 'testdata/test2.zip', 'testdata/test3.zip' ]
als command line arguments.
'''
