public class ShortCircuitDemo1
{
	public static void main( String[] args )
	{
		if ( test1() && test2() )
			System.out.println( "Got 'em both");
		else
			System.out.println("Dang it");
	}
	
	private static boolean test1()
	{
		System.out.println( "execute test1" );
		return true;
	}
	private static boolean test2()
	{
		System.out.println( "execute test2" );
		return true;
	}
}