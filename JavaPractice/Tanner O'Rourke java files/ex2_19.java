public class ex2_19
{
	public static void main( String[] args)
	{
	Vic.reset( args );
	Vic john = new Vic();
	{
		if (john.seesSlot() )
			john.moveOn();
	}
	Vic tim = new Vic();
		if (tim.seesSlot() )
		{
			tim.moveOn();
			if (tim.seesSlot() )
			{
				tim.moveOn();
				if (tim.seesSlot() )
				{
					tim.putCD();
					if (tim.seesCD() )
					{
						tim.moveOn();
						if (tim.seesSlot() )
						{
							tim.putCD();
							if (tim.seesCD() )
							{
								tim.moveOn();
								if (tim.seesSlot() )
								{
									tim.putCD();
								}
							}
						}
					}
				}
			}
		}
	}	
}