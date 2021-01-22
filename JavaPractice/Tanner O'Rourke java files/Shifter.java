public class Shifter extends Vic
{
	public void main shiftThreeToFive
	{
		if ( seesSlot() )
		{
			moveOn();
			if ( seesSlot() )
			{
				moveOn();
				if ( seesCD() )
				{
					takeCD();
					moveOn();
					if ( seesSlot() )
					{
						moveOn();
				}
			}
		}
	}
}