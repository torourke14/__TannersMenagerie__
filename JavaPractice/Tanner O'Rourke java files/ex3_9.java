public class ex3_9 extends Vic
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		ex3_9 tim = new ex3_9();
		tim.fillFirstEmptySlot();
	}
	public void fillFirstEmptySlot()
	{
		String savePos = getPosition();
		while ( seesSlot() && seesCD() )
			moveOn();
		if ( seesSlot() )
			putCD();
			
		while ( !savePos.equals( getPosition() ) )
			backUp();
	}
}