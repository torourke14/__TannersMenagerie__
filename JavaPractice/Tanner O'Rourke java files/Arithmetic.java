public class Arithmetic
{
	public static int larger (int parm1, int parm2)
	{
		int rval      = 0;
		if (parm1 > parm2)
			rval parm1;
		else
			rval = parm2;
		return rval;
	}
	
	public static int smaller(int parm1, int parm2)
	{
		int small = parm1;
		if ( parm2 < small )
			small = parm2;
		return small;
	}
	
	public static int largest(int parm1, int parm2, int parm3)
	{
		int result = parm1;
		if ( parm2 > result )
			result = parm2;
		if ( parm3 > result )
			result = parm3;
		return result;
	}
	
	public static int smallest(int parm1, int parm2, int parm3)
	{
		int 
		if ( parm
	}
	
	public static int absCEO( int parm1 )
	{
		int result = parm1 > 0 ? parm1 : - parm1;
		return result;
	}
	
	public static int abs (int parm1)
	{
		int result = parm1;
		if ( result < 0 )
			result = -result;
	}
	
	public static void
	addTimes (int hour1, int min1, int sec1, int hour2, int min2, int sec2)
	{
	int hourSum = hour1 + hour2;
	int minSum  = min1 + min2;
	int sec Sum = sec1 + sec2;
	
	minSum = minSum + sexSum / 60;
	secSum = secSum % 60;
	
	hourSum = hourSum + minSum / 60;
	minSum = minSum % 60;
	
	hourSum = hourSum % 24;
	System.out.println( hourSum + ":" + min Sum + ":" + secSum + ":";
	
	}
}
