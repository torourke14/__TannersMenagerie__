//Works well!
public class exchp3_1
{
	public static void main( String[] args )
	{
		exchp3_1 tim = new exchp3_1();
		tim.action( 20 );
	}
	public void action ( int count )
	{
		for ( int inx = 0 ; inx < 20 ; ++inx )
		System.out.println( "The square of " + inx + " is " + inx* inx );
	}
}