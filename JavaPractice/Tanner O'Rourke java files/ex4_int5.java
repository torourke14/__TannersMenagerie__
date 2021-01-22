//Works well!
public class ex4_int5 extends Turtle
{
	public static void main( String[] args )
	{
		ex4_int5 tim = new ex4_int5();
			tim.action( 7 );
		
	}
	public void action( int count )
	{
		// most common pattern
		for ( int inx = 0; inx < count ; ++inx )
		{
			say( "hi" );
			move( 0, 20 );
		}	
	}
}