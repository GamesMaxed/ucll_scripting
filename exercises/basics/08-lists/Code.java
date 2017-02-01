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
}
