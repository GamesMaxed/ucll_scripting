class Code
{
    public boolean isBinary(String string)
    {
        for ( char c : string.toCharArray() )
        {
            if ( c != '0' && c != '1' )
            {
                return false;
            }
        }

        return true;
    }
        
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
                // zodat 5 delen door 2 gelijk is aan 2 en niet aan 2.5
                n /= 2;
            }

            return result;
        }
    }

    public int fromBinary(String s)
    {
        int result = 0;

        for ( char c : s.toCharArray() )
        {
            int digit;

            switch ( c )
            {
            case '0':
                digit = 0;
                break;

            case '1':
                digit = 1;
                break;

            default:
                throw new IllegalArgumentException("Invalid digit");
            }
            
            result = result * 2 + digit;
        }

        return result;
    }

    public boolean hasExtension(String filename, String extension)
    {
        extension = "." + extension;
        
        if ( filename.length() < extension.length() )
        {
            return false;
        }
        else
        {
            return filename.substring(filename.length() - extension.length()).equals(extension);
        }
    }
}
