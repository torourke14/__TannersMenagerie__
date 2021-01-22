public class MoveToFront
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		Vic tim = new Vic();
		String pos = tim.getPosition();
	
		while ( tim.seesSlot() )
		{
			tim.moveOn();
		}
		
		while ( !pos.equals( tim.getPosition() ) )
			{
				tim.backUp();
				tim.takeCD();
			}
			
		while ( Vic.stackHasCD() )
		{
			tim.putCD();
			tim.moveOn();
		}
	}
}