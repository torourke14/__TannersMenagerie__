public class GetPositionDemo1
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		Vic tim = new Vic();
		while ( tim.seesSlot() )
		{
		tim.say( tim.getPosition() );
		tim.moveOn();
		}
	}
}