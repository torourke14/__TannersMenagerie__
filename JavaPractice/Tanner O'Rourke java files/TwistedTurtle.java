//Works well!
public class TwistedTurtle extends Turtle
{
	public static void main( String[] args )
	{
		TwistedTurtle twisty = new TwistedTurtle( 45 );
		twisty.paint( 0, 128 );
		
		TwistedTurtle twisted = new TwistedTurtle( 90, 64 );
		twisted.fillCircle( 32 );
		
		TwistedTurtle testy = new TwistedTurtle();
	}
	
	public TwistedTurtle()
	{
		super();
	}
	
	public TwistedTurtle( int degrees )
	{
		move( degrees, 0 );
	}
	
	public TwistedTurtle( int degrees, int distance )
	{
		move( degrees, distance );
	}
}