//Works Well!
public class ForDemo2
{
	public static void main( String[] args )
	{
		System.out.println( factorial( 5 ) );
	}
	private static int factorial  ( int num )
	{
		int rval = 1;
		///////int inx = 0;
		for ( inx = num ; inx > 0 ; --inx )
			rval = rval * inx;
		return rval;
	}
}