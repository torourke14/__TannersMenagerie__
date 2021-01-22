//Works well!
public class EqualsDemo1
{
	public static void main( String[] args )
	{
		String test1 = "my string";
		String test2 = "my ";
		test2 = test2 + "string";
		System.out.println( "Test1 > " + test1 );
		System.out.println( "Test2 > " + test2 );
		//if ( test1 == test2 )
		if ( test1.equals( test2 ) )
			System.out.println ( "equal" );
		else
			System.out.println( "note equal" );
	}
}