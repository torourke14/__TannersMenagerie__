public class ex3_28 extends Vic
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		ex3_28 tim = new ex3_28();
		
		String str1 = tim.getPosition();
		tim.moveOn();
		String str2 = tim.getPosition();
		tim.moveOn();
		
		if ( tim.isAtOneGivenPosition( str1, str2 ) )
			Vic.say( "Yesssss" );
		else
			Vic.say ( "noooooo" );
			
		tim.backUp();
		if ( tim.isAtOneGivenPosition( str1, str2 ) )
			Vic.say( "yessss" );
		else
			Vic.say( "nooooooo" );
		
	}
	
	public boolean isAtOneGivenPosition( String pos1, String pos2 )
	{
		String curPos = getPosition();
		boolean rval = curPos.equals( pos1 ) || curPos.equals( pos2 );
		return rval;
	}
}