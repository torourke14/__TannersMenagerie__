public class Target
{
	public static void main( String[] args )
	{
		Turtle archer = new Turtle();
		
		archer.switchTo( Turtle.RED );
		archer.fillCircle( 300 );
		archer.switchTo( Turtle.YELLOW );
		archer.fillCircle( 200 );
		archer.switchTo( Turtle.BLUE );
		archer.fillCircle( 150 );
		archer.switchTo( Turtle.BLACK );
		archer.fillCircle( 100 );
		archer.switchTo( Turtle.GREEN );
		archer.say( "100" );
		archer.move( 0,125 );
		archer.say( "50" );
		archer.move( 0,50 );
		archer.say( "25" );
		archer.move( 0,75 );
		archer.say( "510" );
	}
}