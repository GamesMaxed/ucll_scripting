public class Code
{
    public int throwDie()
    {
        Random random = new Random();

        // nextInt(n) geeft een getal tussen 0 (inclusief) en n (exclusief)
        return random.nextInt(6) + 1;
    }

    /*
      Gegeven <diceCount> dobbelstenen, wat is de kans dat de
      som der ogen hoger is dan <minimumSum>?
      Men kan dit wiskundig uitrekenen, maar meestal
      is het eenvoudiger om een zogenaamde "Monte-Carlo simulatie" te runnen.
      Dit houdt in dat je een groot aantal keren het experiment
      virtueel uitvoert.
     */
    public double probabilityOfSumHigherThan(int diceCount, int minimumSum, int samples)
    {
        Random random = new Random();
        int count = 0;

        for ( int i = 0; i != samples; ++i )
        {
            int sum = 0;

            for ( int j = 0; j != diceCount; ++j )
            {
                sum += random.nextInt(6) + 1;
            }

            if ( sum >= minimumSum )
            {
                count++;
            }
        }

        return ((double) count) / samples;
    }
}
