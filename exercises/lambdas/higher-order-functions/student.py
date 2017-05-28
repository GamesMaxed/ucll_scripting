def count(xs: list, predicate):
    """
    Gegeven een lijst xs en een functie predicate,
    telt het aantal elementen uit xs waarvoor
    predicate een truthy waarde teruggeeft.
    """
    count = 0
    for x in xs:
        if predicate(x):
            count += 1
    return count


def find_first(xs: list, predicate, default = None):
    """
    Gegeven een lijst xs, een functie predicate
    en een waarde default, zoekt naar
    het eerste element uit xs waarvoor
    predicate een truthy value teruggeeft.
    Indien geen elementen gevonden
    kan worden, wordt default teruggegeven.
    """
    for x in xs:
        if predicate(x):
            return x
    return default


def filter(xs: list, predicate):
    """
    Gegeven een lijst en een functie predicate,
    geeft een lijst van alle elementen van
    xs terug waarvoor predicate een truthy value
    teruggeeft.
    Deze elementen dienen in dezelfde volgorde
    te staan als in xs.
    """
    filteredList = list()
    for x in xs:
        if predicate(x):
            filteredList.append(x)

    return filteredList


def all(xs: list, predicate):
    """
    Gegeven een lijst xs en een functie predicate,
    geeft een truthy waarde terug indien
    predicate een truthy waarde teruggeeft
    voor elke x uit xs.
    In het andere geval wordt een falsey waarde
    teruggegeven.
    """
    for x in xs:
        if not predicate(x):
            return False
    return True

def any(xs, predicate):
    """
    Gegeven een lijst xs en een functie predicate,
    geeft een truthy waarde terug indien
    predicate een truthy waarde teruggeeft
    voor een x uit xs.
    In het andere geval wordt een falsey waarde
    teruggegeven.
    """
    for x in xs:
        if predicate(x):
            return True
    return False


def group_by_key(xs: list, key_function):
    """
    Gegeven een lijst xs en een functie key_function,
    groepeert alle elementen samen waarvoor
    key_function eenzelfde waarde geeft.
    Het resultaat wordt teruggegeven
    als een dictionary waarvan 
    * de keys gelijk zijn aan de waarden van key_function
    * de values lijsten zijn van elementen uit xs
      waarvoor key_function de key voor teruggaf.

    Bijvoorbeeld, stel key_function zijnde een functie
    die 'even' teruggeeft voor even getallen
    en 'odd' voor oneven getallen, 
    Voor xs = [1, 2, 3, 4] krijgen we dan als resultaat
    de volgende dictionary:
      { 'even': [2, 4], 'odd': [1, 3] }
    """
    result = dict()

    for value in xs:
        key = key_function(value)
        if key not in result:
            result[key] = list()
        result[key].append(value)

    return result


#
# UITDAGING
#
def memoize(function):
    """
    Memoization is een algemeen toepasbare techniek
    om aan snelheid te winnen in ruil voor extra geheugenverbruik.
    Stel dat je een 'stateless' functie hebt, d.i.
    een functie die gegeven dezelfde argumenten

    altijd dezelfde waarde teruggeeft.
    Bv. beschouw de volgende code:
           print(f(1))
           print(f(1))
           print(f(1))
    Bij een stateless functie is het zo dat er 3x hetzelfde
    wordt afgeprint. Functies voor wie dat niet het geval
    is, zijn stateful.

    Stel nu dat je een rekenintensieve stateless functie hebt:
    telkens je de functie oproept duurt het 10 seconden
    eer je je resultaat hebt. Je weet echter dat je de functie
    vaak opnieuw zult oproepen met dezelfde argumenten.
    In dat geval is het interessant om de resultaten
    van de functie bij te houden, zodat je wanneer
    je de functie een tweede keer oproept
    met dezelfde argumenten, je het oude resultaat
    gewoon kunt opzoeken en teruggeven i.p.v.
    alles opnieuw te berekenen.

    Schrijf de functie memoize die, gegeven een
    stateless functie F, een nieuwe functie G teruggeeft
    die dezelfde resultaten produceert als F,
    maar de resultaten bijhoudt in een tabel.
    De eerste keer dat de functie G opgeroepen wordt
    met argument X, moet G vragen aan F wat het resultaat is.
    De 2de keer dat met G(X) uitrekent, moet G zich
    herinneren dat dit reeds gebeurde in het verleden
    en het vorige resultaat teruggeven zonder beroep
    te doen op F.

    Je hoeft enkel unaire functies te ondersteunen.
    M.a.w. je mag ervan uitgaan dat de functie F
    exact 1 argument heeft.
    """
    cache = {}

    def memoized(x):
        nonlocal cache
        if x in cache:
            return cache[x]
        else:
            result = function(x)
            cache[x] = result
            return result

    return memoized


#
# UITDAGING
#
def create_change_detector():
    """
    Geeft een functie F terug die zich als volgt gedraagt:
    F onthoudt welk argument het krijgt van oproep tot oproep.
    Indien het argument gelijk is aan dat van de vorige oproep,
    dan geeft F False terug. Indien het argument verschilt
    van dat van de vorige oproep, dan geeft F True terug.
    Bij de eerste oproep geeft F True terug.

    Bijvoorbeeld:
    F = create_change_detector()

    F(1)  # True
    F(1)  # False
    F(1)  # False
    F(2)  # True
    F(2)  # False
    F(1)  # True
    F(2)  # True
    F(2)  # False
    """
    last = None
    is_first = True

    def wrapper(x):
        nonlocal last
        nonlocal is_first

        if is_first or x != last:
            is_first = False
            last = x
            return True
        else:
            return False

    return wrapper