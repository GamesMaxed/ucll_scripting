import java.util.*;


public class Code
{
    /*
      Een String[] laat toe om gegeven een index snel de String op die positie
      terug te vinden. Stel dat we het inverse nodig hebben: we willen, gegeven een
      String, snel weten waar die gepositioneerd is in de array.
      M.a.w., gegeven een String s moeten we de (kleinste) index i terugkrijgen zodat
      strings[i] gelijk is aan s.
     */
    public HashMap<String, Integer> inverseLookup(String[] strings)
    {
        // Een map die strings associeert met integers
        HashMap<String, Integer> result = new HashMap<>();

        // Array afgaan
        for ( int i = 0; i != strings.length; ++i )
        {
            String string = strings[i];

            // Kijken of de string al eerder voorkwam in de array
            // Indien dit het geval is, moeten we de eerdere string-index associatie behouden.
            if ( !result.containsKey(string) )
            {
                // String koppelen met index i
                result.put(string, i);
            }
        }

        return result;
    }

    /*
      Zoekt de geassocieerde waarde van key in map. Indien deze associatie
      niet bestaat, moet defaultValue teruggegeven worden.
     */
    public String getWithDefault(HashMap<String, String> map, String key, String defaultValue)
    {
        if ( map.containsKey(key) )
        {
            return map.get(key);
        }
        else
        {
            return defaultvalue;
        }
    }

    /*
      Telt hoe vaak element voorkomt in de gegeven ArrayList.
      Bv. ['a', 'b', 'b'] moet { 'a' => 1, 'b' => 2 } opleveren.
     */
    public HashMap<String, Integer> countFrequencies(ArrayList<String> strings)
    {
        HashMap<String, Integer> result = new HashMap<>();

        for ( String string : strings )
        {
            // Eerst nagaan of string eerder voorkwam
            if ( result.containsKey(string) )
            {
                // String kwam eerder voor; incrementeer frequentie
                int oldFrequency = result.get(string);
                result.put(string, oldFrequency + 1);
            }
            else
            {
                // Eerste keer dat string voorkwam; frequentie op 1 zetten
                result.put(string, 1);
            }
        }

        return result;
    }

    /*
      Zoekt naar associatie van key in de eerste stylesheet uit de lijst.
      Indien deze bestaat, geeft de overeenkomstige waarde terug.
      Indien deze niet bestaat, wordt verder gezocht in de volgende stylesheet in de lijst.
      Indien geen enkele stylesheet de key bevat wordt defaultValue teruggegeven.
     */
    public String cssLookup(ArrayList<HashMap<String, String>> styleSheets, String key, String defaultValue)
    {
        for ( HashMap<String, String> styleSheet : styleSheets )
        {
            if ( styleSheet.containsKey(key) )
            {
                return styleSheet.get(key);
            }
        }

        return defaultValue;
    }
}
