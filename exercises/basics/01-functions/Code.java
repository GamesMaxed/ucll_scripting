class Code
{
    /*
      De vertaling van deze methode krijg je cadeau.
      Gebruik het als inspiratie om square te vertalen.
     */
    public int increment(int x)
    {
        return x + 1;
    }
    
    
    /*
      Java heeft aparte methodes nodig om ints en doubles
      te kunnen kwadrateren.
      In Python kan square voorgesteld door een enkele functie.

      Java ondersteunt geen "losse" functies: ze moeten altijd
      horen bij een klasse. Python laat daarentegen
      wel "losse" functies toe. Implementeer
      square als zulk een functie.
     */
    public int square(int x)
    {
        return x * x;
    }

    public double square(double x)
    {
        return x * x;
    }

    
    public boolean areOrdered(int x, int y, int z)
    {
        return (x <= y && y <= z) || (x >= y && y >= z);
    }


    public boolean isDivisibleBy(int x, int y)
    {        
        return y != 0 && x % y == 0;
    }
}
