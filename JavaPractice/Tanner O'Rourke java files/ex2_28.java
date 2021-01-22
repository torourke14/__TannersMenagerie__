public class ex2_28 extends ex2_28Test
{
	public boolean seesTwoFilled()
	{
		boolean rval = false;
		
		if ( seesSlot() )
		{
			if ( seesCD() )
			{	
				moveOn();
				if ( seesSlot() )
					if ( seesCD() )
						rval = true;
				backUp();
			}
		}
		return rval;		
	}
}