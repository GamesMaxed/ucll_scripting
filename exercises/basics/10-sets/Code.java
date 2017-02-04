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

    public ArrayList<String> removeDuplicates(ArrayList<String> strings)
    {
        HashSet<String> found = new HashSet<>();
        ArrayList<String> result = new ArrayList<>();

        for ( String string : strings )
        {
            if ( !found.contains(string) )
            {
                result.add(string);
                found.add(string);
            }
        }

        return result;
    }
}
