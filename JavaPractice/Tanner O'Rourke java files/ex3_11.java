public class ex3_11 extends Vic
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		ex3_11 tim = new ex3_11();
	}
	public void fillLastEmptySlot()
	{
		String savePos = getPosition();
		String lastEmpty = savePos;
		
		while ( seesSlot() )
		{
			if ( !seesCD() )
				lastEmpty = getPosition();
			moveOn();
		}
		
		while ( !lastEmpty.equals( getPosition() ) )
			backUp();
		if ( !seesCD() )
			putCD();
			
		while( !savePos.equals( getPosition() ) )
			backUp();
	}
}