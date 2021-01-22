public class WhileDemo1
{
	public static void main( String[] args )
	{
		Vic tim = new Vic();
		while ( tim.seesSlot() )
		{
			tim.moveOn();
			Vic.say ( "weeee" );
		}
	}
}