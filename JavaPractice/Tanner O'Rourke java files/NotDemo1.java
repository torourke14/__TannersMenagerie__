public class NotDemo1
{
	public static void main( String[] args )
	{
		Vic tim = new Vic();
		Vic fred = new Vic();
		
		if (tim.seesSlot() )
			Vic.say( "tim sees a slot" );
		else
			Vic.say( "tim doesn't see a slot" );
		
		if (!fred.seesSlot() )
			Vic.say( "Fred doesn't see a slot" );
		else
			Vic.say( "fred sees a slot" );
	}
}