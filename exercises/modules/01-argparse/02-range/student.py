'''
Schrijf een script dat gebruikt kan worden om getallen af te printen.
Het script ondersteunt de volgende argumenten:

    --init      Beginwaarde. Optioneel, standaardwaarde 0.
    --to        Eindwaarde. Verplicht.
    --step      Stapwaarde. Optioneel, standaardwaarde 1.


Voorbeeld 1

    python student.py --to 5

geeft

    0
    1
    2
    3
    4
    5


Voorbeeld 2

    python student.py --init 2 --to 10 --step 2

drukt af

    2
    4
    6
    8
    10


Steun op de module argparse (zoek informatie online en experimenteer)
om de command line arguments te parsen. Bijvoorbeeld,

    parser = argparse.ArgumentParser()
    parser.add_argument('--to', type=int, required=True)
    args = parser.parse_args()

zorgt ervoor dat je script een parameter "--to N" verwacht, waarbij
N een integer is. De variabele args bevat nadien een object
met veld 'to'. Bijvoorbeeld,

    python student.py --to 42

zorgt ervoor dat args.to gelijk is aan 42. Lees de documentatie
van argparse om te weten te komen hoe je optionele parameters kan instellen.
'''
