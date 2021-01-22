public class VicPlus extends Vic
{
	public boolean goToLastCD()
	{
		String savePos = getPosition();
		boolean rval = false;
		while ( seesSlot() )
		{
			if ( seesCD() )
			{
				savePos = getPosition();
				rval = true;
			}
			moveOn();
		}
		
		while ( !savePos.equals( getPosition () ) )
			backUp();
			return rval;
	}
	
	public boolean canTakeCD()
	{
		if ( seesSlot() )
			if ( seesCD() )
				return true;
			else
				return false;
		else
			return false;
	}
}