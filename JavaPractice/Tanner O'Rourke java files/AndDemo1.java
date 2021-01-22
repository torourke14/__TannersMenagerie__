public class AndDemo1
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		Vic tim = new Vic();
		tim.moveOn();
		if ( tim.seesSlot() && tim.seesCD() )
			Vic.say( "Got a CD" );
		else
			Vic.say( "No tunes for Tim" );
	}
}