class Monotone
{
    public boolean monotone(int x, int y, int z)
    {
        return (x <= y && y <= z) || (x >= y && y >= z);
    }
}
