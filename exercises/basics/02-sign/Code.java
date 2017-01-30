class Code
{
    public int abs(int x)
    {
        if ( x < 0 ) return -x;
        else return x;
    }
    
    public int sign(int x)
    {
        if ( x < 0 ) return -1;
        else if ( x == 0 ) return 0;
        else return 1;
    }
}
