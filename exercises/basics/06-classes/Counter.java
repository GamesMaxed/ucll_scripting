class Counter
{
    // Zoek op hoe je velden private maakt
    private int x;

    // Zoek op hoe je een constructor definieert
    public Counter()
    {
        this.x = 0;
    }

    public int current()
    {
        return x;
    }

    public void increment()
    {
        // Opgelet: Python heeft geen increment operator
        x++;
    }

    public void reset()
    {
        x = 0;
    }
}
