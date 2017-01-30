public class Fraction
{
    private int numerator;
    private int denominator;

    private int gcd(int x, int y)
    {
        if ( x < 0 ) return gcd(-x, y);
        else if ( y < 0 ) return gcd(x, -y);
        else if ( y == 0 ) return x;
        else return gcd(y, x % y);
    }

    public Fraction(int numerator, int denominator)
    {
        if ( denominator == 0 )
        {
            // In Python: RuntimeError
            throw new IllegalArgumentException("Denominator must not be 0");
        }
        else
        {
            int gcd = this.gcd(numerator, denominator);

            if ( denominator < 0 )
            {
                numerator = -numerator;
                denominator = -denominator;
            }
            
            this.numerator = numerator / gcd;
            this.denominator = denominator / gcd;
        }
    }

    // Implementeer dit als property 'numerator' met enkel een getter
    public int getNumerator()
    {
        return this.numerator;
    }

    // Implementeer dit als property 'denominator' met enkel een getter
    public int getDenominator()
    {
        return this.denominator;
    }

    // Implementeer dit als __add__ (underscores maken deel uit van de naam)
    // Deze methode kan je oproepen met de standaard + syntax: "a + b" ipv "a.add(b)"
    public Fraction add(Fraction that)
    {
        int numerator = this.numerator * that.denominator + that.numerator * this.denominator;
        int denominator = this.denominator * that.denominator;

        return new Fraction(numerator, denominator);
    }

    // Implementeer dit als __neg__
    public Fraction negate()
    {
        return new Fraction(-numerator, denominator);
    }

    // Implementeer dit als __sub__
    public Fraction subtract(Fraction that)
    {
        return add(that.negate());
    }

    // Implementeer dit als __mul__
    public Fraction multiply(Fraction that)
    {
        int numerator = this.numerator * that.numerator;
        int denominator = this.denominator * that.denominator;

        return new Fraction(numerator, denominator);
    }

    public Fraction inverse()
    {
        return new Fraction(denominator, numerator);
    }

    // Implementeer dit als __truediv__
    public Fraction divide(Fraction that)
    {
        return multiply(that.inverse());
    }
}
