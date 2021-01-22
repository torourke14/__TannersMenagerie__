public class ex2_14
{
	public static void main (String[] args )
	{
		Vic.reset( args );
		Vic john = new Vic();
		
		if (john.seesSlot() )
		{
			john.moveOn();
			if (john.seesSlot() )
			{
				john.moveOn();
				if (john.seesSlot() )
				{
					john.moveOn();
					if (john.seesCD() )
					{
						john.takeCD();
						if (john.seesSlot() )
						{
							john.moveOn();
							if (john.seesCD() )
							{
								john.takeCD();
							}
						}	
					}	
				}
			}
		}
	}
}