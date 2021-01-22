public class Looper extends Vic
{
	public void fillSlots()
	{
		String savePos = getPosition();
		while ( seesSlot() )
		{
			putCD();
			moveOn();
		}
		backUpTo( savePos );
	}
	
	public void clearSlotsToStack()
	{
		String savePos = getPosition();
		
		while ( seesSlot() )
		{
		putCD();
		moveOn();
		}
	}
	public void fillEvenSlots()
	{
		if ( seesSlot() )
		{
			moveOn();
			fillOddSlots();
			backUp();
		}
	}
		
	public void fillOddSlots()
	{
		String pos = getPosition();
		while ( seesSlot() && stackHasCD() )
		{
			putCD();
			moveOn();
			if ( seesSlot() );
				moveOn();
		}
		backUpTo ( pos );
	}
	
	public boolean seesAllEvensFilled()
	{
		boolean rcode = false;
		if ( seesSlot() )
		{
			moveOn();
			rcode = seesOddsFilled(); //seesOddsFilled isn't made yet
			backUp();
		}
		return rcode;
	}
	
	private void backUpTo( String pos )
	{
		while ( !pos.equals( getPosition() ) )
			backUp();
	}
}