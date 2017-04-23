'''
Schrijf een script dat de inhoud van een bestand afprint.
De command line parameters zijn

    file           Naam af te printen bestand. Verplicht.
    --start N      Index van eerste af te printen regel.
                   Begint te tellen bij 0. Optioneel, standaard 0.
    --end N        Index van de laatst af te printen regel.
                   Optioneel, standaard is dit oneindig (m.a.w. standaard
                   wordt het bestand tot en met de laatste regel afgeprint)
    --skip-empty   Lege regels mogen niet afgeprint worden.
                   Een lege regel is een regel die geen niet-whitespace teken bevat,
                   m.a.w. een regel van lengte 0 of een regel die enkel
                   whitespace bevat worden aanzien als leeg.
                   Optioneel, standaard staat de optie af.

Voorbeelden:
    python student.py file.txt
    python student.py file.txt --start 5 --end 10 --skip-empty


file is een positionele parameter; dit betekent
dat er geen parameternaam voorafgaat. Zo moet
    python student.py file.txt
geschreven worden, en niet
    python student.py --file file.txt
Positionele argumenten kan je definiëren met
    parser.add_argument('file')


--skip-empty verwacht geen argument, het is dus
    python student.py file.txt --skip-empty
en niet
    python student.py file.txt --skip-empty true
Je kan deze definiëren met
     parser.add_argument('--skip-empty', action='store_true')
'''
