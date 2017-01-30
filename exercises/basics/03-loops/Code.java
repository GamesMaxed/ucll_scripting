public class Code
{
    public boolean isPrime(int n)
    {
        for ( int i = 2; i <= n; ++i )
        {
            if ( n % i == 0 )
            {
                return false;
            }
        }

        return n > 1;
    }

    public int countPrimesBelow(int n)
    {
        int count = 0;
        
        for ( int i = 0; i < n; ++i )
        {
            if ( isPrime(n) )
            {
                // Python heeft geen ++ operator
                ++count;
            }
        }

        return count;
    }

    public int gcd(int x, int y)
    {
        // Gebruik de reeds bestaande Python functies voor abs en max
        x = Math.abs(x);
        y = Math.abs(y);

        // min bestaat reeds in Python
        for ( int i = Math.max(x, y); i > 0; --i )
        {
            if ( x % i == 0 && y % i == 0 )
            {
                return i;
            }
        }

        return 0;
    }
}
