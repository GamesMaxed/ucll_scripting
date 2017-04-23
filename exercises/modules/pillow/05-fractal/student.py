'''
Voor deze opgave genereren jullie de Mandelbrot fractal.
  http://tilde.club/~david/m/#

Je kan zelf afbeeldingen genereren:

  python solution.py --center '(-0.5,0)' --domain-size 2 --image-size 500
  python solution.py --center '(-0.088,0.654)' --domain-size 0.01 --image-size 500
'''



class Complex:
    '''
    Zoals een breuk kan worden gemodelleerd door
    een klasse met 2 velden (teller en noemer),
    kan een complex getal eveneens voorgesteld
    worden door een koppel getallen, doorgaans
    're' en 'im' genoemd.

    De notatie voor een breuk is teller/noemer.
    Voor een complex getal is dit re + im i,
    waarbij i een symbool zoals pi is.
    Bijvoorbeeld, 5+3i is een complex
    getal met re=5 en im=3.

    Waar bij een breuk teller en noemer
    gehele getallen zijn, is kunnen bij complexe getallen
    re en im willekeurige reële getallen zijn.

    Een complex getal stelt ook iets heel anders voor
    dan een breuk. De eenvoudigste interpretatie
    is om een complex getal te visualiseren
    als een 2D punt, waarbij de x- en y-coördinaat
    overeenkomen met re en im, respectievelijk.
    Dit aspect is belangrijk voor deze opgave.
    Zo komt 0+0i overeen met de oorsprong,
    1+0i met (1,0),  0+1i met (0,1), etc.

    Er zijn tal van operaties gedefinieerd op complexe getallen.
    Voor deze opgave zijn we slechts geïnteresseerd
    in optelling, vermenigvuldiging en absolute waarde.
    '''
    
    def __init__(self, re, im):
        '''
        Constructor.
        '''
        raise NotImplementedError()

    def __add__(self, other):
        '''
        Het optellen van a+bi met c+di geeft als resultaat
        (a+c) + (b+d)i, m.a.w. de re's worden samen opgeteld,
        alsook de ims, en deze sommen vormen de nieuwe
        re en im van het resultaat.

        Zie https://en.wikipedia.org/wiki/Complex_number#Addition_and_subtraction
        '''
        raise NotImplementedError()

    def __mul__(self, other):
        '''
        Deze operatie is wat ingewikkelder. We verwijzen je naar
        https://en.wikipedia.org/wiki/Complex_number#Multiplication_and_division
        '''
        raise NotImplementedError()

    def abs(self):
        '''
        De absolute waarde van een complex getal komt overeen
        met de afstand tot de oorsprong.
        https://en.wikipedia.org/wiki/Complex_number#Absolute_value_and_argument
        '''
        raise NotImplementedError()


def mandelbrot(c, max_steps, bound):
    '''
    Een lange uitleg voor wat uiteindelijk een simple lus moet worden...

    De parameter c is een complex getal dat zoals eerder uitgelegd
    overeenkomt met een punt in het 2D vlak.
    Men neemt een complex getal z1 = c.
    Op deze z1 voert men een operatie uit:

      z2 = z1 * z1 + c

    Dit geeft een nieuw complex getal z2 als resultaat.
    Men voert dan weer dezelfde operatie uit op z2, dit geeft z3.

      z3 = z2 * z2 + c
      z4 = z3 * z3 + c
      z5 = z4 * z4 + c
      ...

    Zodoende krijgt men een lange reeks complexe getallen
    dat men kan interpreteren als een pad dat begint in z1
    en dan rondspringt naar z2, z3, z4, ...

    Er zijn nu twee mogelijkheden:
      * het pad convergeert, wat betekent dat het een eindbestemming heeft
      * het pad divergeert, wat betekent dat het doelloos alsmaar verder weg gaat

    De meeste paden zullen divergeren. Om de fractal te genereren, zijn we geïnteresseerd
    in *hoe snel* het pad divergeert.

    Hoe meten we dit? We beginnen met z1, en rekenen vervolgens z2, z3, z4, ... uit.
    Zolang deze z-waarden 'dichtbij' de oorsprong blijven, doen we voort.
    Eenmaal we een z-waarde vinden die zich 'te ver af' bevindt, stoppen we.
    Wat we beschouwen als 'dichtbij' en 'te ver' is vrij arbitrair.
    De parameter bound is wat zal bepalen waar de grens ligt:
    zolang z.abs() <= bound, doen we voort. Van zodra z.abs() > bound, stoppen we.
    
    Het kan zijn dat het heel lang duurt voordat de z-waarden voorbij deze bound
    springen. Misschien gebeurt dat zelfs nooit. Daarom is het nodig
    om een maximum op te leggen op het aantal z-waarden dat we uitrekenen.
    Dit maximum wordt gegeven door max_steps.

    Concreet ziet het algoritme er dus zo uit:

      Initialiseer z = c
      Herhaal maximum max_steps keer:
        z = z * z + c
        Indien z.abs() > bound, stop met itereren

    De functie moet als resultaat teruggeven:

        aantal_stappen / max_steps

    waarbij aantal_stappen gelijk is aan het aantal z-waarden
    is dat men moest uitrekenen eer z.abs() > bound.
    aantal_stappen wordt tevens maximaal max_steps groot.
    '''
    raise NotImplementedError()



class Projection:
    '''
    Deze klasse krijg je cadeau.
    Ze dient om pixelcoördinaten om te zetten naar een complex getal.
    '''
    
    def __init__(self, image_size, center, size):
        '''
        Constructor.

        image_size      Een integer die de breedte en hoogte van de bitmap voorstelt

        center          Een (x, y) koppel dat aangeeft met welk punt
                        het centrum van de afbeelding overeenkomt.

        size            Een positieve double dat aangeeft hoe fel gezoomd werd.
                        Hoe *kleiner* het getal, hoe *meer* ingezoomd het beeld is.
        '''
        cx, cy = center
        self.left = cx - size / 2
        self.top = cy + size / 2
        self.size = size
        self.dx = size / image_size
        self.dy = size / image_size

    def at(self, x, y):
        '''
        Zet pixelcoördinaten om naar een complex getal.
        '''
        px = self.left + self.dx * x
        py = self.top - self.dy * y

        return Complex(px, py)
    


def generate_image(image_size, projection, max_steps, bound):
    '''
    Maakt een afbeelding aan van image_size x image_size groot.
    Vervolgens wordt voor elke pixel een kleur uitgerekend als volgt:
    voor elke pixel op positie (x, y) wordt het overeenkomstige
    complex getal uitgerekend; hiervoor wordt projection.at gebruikt.
    Dit complex getal wordt aan de mandelbrot-functie meegegeven,
    wat een getal tussen 0 en 1 oplevert.
    Op basis van dit resultaat wordt een kleur uitgerekend.
    De eenvoudigste manier is gebruik te maken van grijswaarden.
    Stel dat r het resultaat van de mandelbrot functie is,
    dan kunnen we deze omzetten naar een grijswaarde
    met de volgende berekening:

      c = int(r * 255)
      color = (c, c, c)

    Deze kleur wordt dan toegekend aan de pixel op positie (x, y).
    '''
    raise NotImplementedError()


'''
Command line options:

  --output            Naam van uitvoerbestand
  --center (x,y)      Het centrum van de fractal. x en y moeten meegegeven worden aan de Projection constructor
  --image-size N      Grootte van de afbeelding (zowel grootte als breedte; we ondersteunen enkel vierkantige resultaten)
  --domain-size N     Zoomlevel. Moet worden meegegeven aan Project constructor.
  --max-iterations N  Maximum aantal iteraties. Optioneel, standaard 100.
  --bound N           Maximum afstand tot oorsprong. Optioneel, standaard 10.0.
'''
if __name__ == '__main__':
    raise NotImplementedError()
