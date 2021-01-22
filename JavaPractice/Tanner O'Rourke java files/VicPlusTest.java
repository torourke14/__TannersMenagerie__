public class VicPlusTest
{
	public static void main( String[] args )
	
	{
		Vic.reset( args );
		VicPlus plussy = new VicPlus();
		
		if( plussy.goToLastCD() )
			Vic.say( "got one" );
		else
			Vic.say( "dang it" );
	}
}