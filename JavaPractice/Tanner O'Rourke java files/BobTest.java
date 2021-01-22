public class BobTest
{
	public static void main( String[] args )
	{
		Bob robert = new Bob();
		robert.whoareyou();
		robert.paint( 45,256 );
		Turtle toots = new Bob();
		
		SmartTurtle john = new SmartTurtle();
		john.makeSmallSquare();
		
		SmartTurtle bob = new SmartTurtle();
		bob.move ( 0,100 );
		bob.makeSmallSquare();
	}
}