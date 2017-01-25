Voor deze oefeningen krijg je een lijst van strings die voldoen aan een bepaald patroon.
Je moet zelf ontdekken welk patroon dit is en hiervoor een regular expression opstellen.

Voorbeeld
---------
Je krijgt als strings die voldoen aan het patroon

   'a'
   'aa'
   'aaa'
   'aaaa'
   'aaaaa'

Je krijgt tevens strings die niet voldoen aan het patroon:

   ''
   'b'
   ' a'
   'a '
   'aaaxaaa'

Hieruit kan je afleiden dat het patroon waar je naar op zoek bent
"een of meerdere a's" is. In regex vorm is dit

     a+


Voor elke oefening moet je een functie

     def riddleN(string):
         ...

schrijven die nagaat of string voldoet aan het patroon.
Voor bovenstaand voorbeeld zou de implementatie zijn:

     def riddle0(string):
         return re.fullmatch(r'a+', string)

(De 0 in 'riddle0' werd vrij gekozen, dit getal hangt af van welke oefening je maakt)


De strings kan je terugvinden in tests.py. Voor bovenstaand voorbeeld zou je vinden:

    with riddle(0):       # <-- 0 = nummer van oefening
        match('a')        # <-- strings die wel voldoen aan het patroon
        match('aa')
        match('aaa')
        match('aaaa')
        match('aaaaa')

        noMatch('')       # <-- strings die niet voldoen aan het patroon
        noMatch('b')
        noMatch(' a')
        noMatch('a ')
        noMatch('aaaxaaa')
