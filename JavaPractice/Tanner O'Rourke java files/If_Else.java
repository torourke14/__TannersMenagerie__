public class If_Else extends Vic
{
	public static void main( String[] args )
	{
		Vic.reset( args )
		If_Else slim = new If_Else();
		slim.downShift();
	}
	public void downShift()
	{
		if (seesSlot() )
		{
			if( seesCD() )
			{
				takeCD();
				moveOn();
				if(seesSlot() )
					putCD();
			}
		}
	}
}