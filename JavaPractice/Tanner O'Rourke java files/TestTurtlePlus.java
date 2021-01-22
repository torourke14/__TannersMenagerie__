public class TestTurtlePlus
{
	public static void main( String[] args )
	{
		TurtlePlus plussy = new TurtlePlus();
		if ( plussy.areYouATurtle() )
			plussy.say( "I am a Turtle" );
			plussy.paint( 0,64 );
		if ( plussy.areYouARabbit() )
			plussy.say( "I am a rabbit" );
			plussy.fillCircle( 10 );
	}
}