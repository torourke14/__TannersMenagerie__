public class ex3_1 extends Vic
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		ex3_1 tim = new ex3_1();
		tim.removeAllCDs();
	}
	
	public void removeAllCDs()
	{
		while ( seesSlot() || seesCD() )
			{
				takeCD();
				moveOn();
			}
	}
}

