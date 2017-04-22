'''
Schrijf een script dat, gegeven de volgende parameters

    files       Positionele parameters; lijst van grafische bestanden
    --size N    Grootte N. Optioneel, standaard 64.

een thumbnail van grootte NxN van elk van de gegeven bestanden genereert
en wegschrijft. De thumbnails moet dezelfde extensie hebben als het oorspronkelijke
bestand en de bestandsnaam krijgt een suffix -thumbnail om het te onderscheiden
van het origineel. Bijvoorbeeld, de thumbnail van x.png moet x-thumbnail.png heten.

Gebruik het prepare commando om testdata te downloaden.


Bijvoorbeeld,

    python student.py a.jpg b.png

produceert

    a-thumbnail.jpg
    b-thumbnail.png

dewelke 64x64 versies zijn van a.jpg en b.png, respectievelijk.
'''
