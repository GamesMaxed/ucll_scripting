class ToBinary
{
    public String toBinary(int n)
    {
        if ( n < 0 )
        {
            // Gebruik RuntimeError in Python
            throw new IllegalArgumentException("n must be positive");
        }
        else if ( n == 0 )
        {
            return "0";
        }
        else
        {
            String result = "";

            while ( n > 0 )
            {
                // Bij het optellen van een getal en een string zal Java
                // het getal vanzelf omzetten naar stringvorm
                // Python is echter strenger en verwacht dat je zelf
                // expliciet het getal omzet naar een string
                result = (n % 2) + result;

                // Let op: in Python moet je expliciet kiezen voor integer division
                // zodat 5 delen door 2 gelijn is aan 2 en niet aan 2.5
                n /= 2;
            }

            return result;
        }
    }
}
