//Works well!

public class ex3_29 extends Vic
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		ex3_29 tim1 = new ex3_29();
		Vic    tim2 = new Vic();
		tim1.moveToCorrespondingSlot( tim2 );
	}
	
	public void moveToCorrespondingSlot( Vic param )
	{
		while ( seesSlot() && param.seesSlot() )
		{
			if ( seesCD() && !param.seesCD() )
			{
				takeCD();
				param.putCD();
			}
			moveOn();
			param.moveOn();
		}
	}
}