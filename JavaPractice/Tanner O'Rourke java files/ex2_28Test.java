public class ex2_28Test extends Vic
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		ex2_28 tim = new ex2_28();
		tim.seesTwoFilled();
		
		if( tim.seesTwoFilled() )
			Vic.say( "two filled!" );
		else
			Vic.say( "only one filled" );
	}
}