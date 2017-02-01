class Person
{
    private double weight;
    private double height;
    
    public Person(double weight, double height)
    {
        setWeight(weight);
        setHeight(height);
    }

    public double getWeight()
    {
        return weight;
    }

    public void setWeight(double weight)
    {
        if ( weight < 0 )
        {
            throw new IllegalArgumentException("Invalid weight");
        }
        else
        {
            this.weight = weight;
        }
    }

    public double getHeight()
    {
        return height;
    }

    public void setHeight(double height)
    {
        if ( height < 0 )
        {
            throw new IllegalArgumentException("Invalid height");
        }
        else
        {
            this.height = height;
        }
    }

    public double bmi()
    {
        return weight / (length * length);
    }
}
