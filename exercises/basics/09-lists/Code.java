import java.util.ArrayList;


public class Code
{
    public int sum(ArrayList<Integer> ns)
    {
        int total = 0;

        for ( int n : ns )
        {
            total += n;
        }

        return total;
    }

    public ArrayList<Integer> interval(int a, int b)
    {
        ArrayList<Integer> result = new ArrayList<>();

        for ( int i = a; i <= b; ++i )
        {
            result.add(i);
        }

        return result;
    }

    public int maximum(ArrayList<Integer> ns)
    {
        // Python: gebruik -math.inf
        int result = Integer.MIN_VALUE;

        for ( int n : ns )
        {
            result = Math.max(result, n);
        }

        return result;
    }

    public ArrayList<Integer> factors(int n)
    {
        ArrayList<Integer> result = new ArrayList<Integer>();

        n = Math.abs(n);

        int k = 2;
        while ( n > 1 )
        {
            if ( n % k == 0 )
            {
                result.add(k);
                n /= k;
            }
            else
            {
                ++k;
            }
        }

        return result;
    }

    public void removeShortStrings(ArrayList<String> strings, int minimumLength)
    {
        for ( int i = strings.size(); i >= 0; --i )
        {
            if ( strings.get(i).length() < minimumLength )
            {
                strings.remove(i);
            }
        }
    }
}
