import java.util.*;

public class Code
{
    public HashSet<Integer> createInterval(int from, int to)
    {
        HashSet<Integer> result = new HashSet<>();

        for ( int i = from; i <= to; ++i )
        {
            result.add(i);
        }

        return result;
    }
}
