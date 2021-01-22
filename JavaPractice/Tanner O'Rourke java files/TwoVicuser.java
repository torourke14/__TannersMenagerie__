// Works Well!

public class TwoVicuser extends Vic
{
	public static void main ( String[] args )
	{
		Vic.reset( args );
		TwoVicuser jane = new TwoVicuser();
		TwoVicuser sally = new TwoVicuser();
		if ( jane.hasAsManySlotsAs( sally ) )
			Vic.say( "jane and Sally have happiness" );
		else
			Vic.say( "jane is mad at sally" );
	}
	public boolean hasAsManySlotsAs ( Vic parm )
	{
		String pos = getPosition();
		while ( this.seesSlot() && parm.seesSlot() )
		{
			moveOn();
			parm.moveOn();
		}
		boolean rval = !seesSlot() && !parm.seesSlot();
		while ( !pos.equals( getPosition() ) )
		{
			backUp();
			parm.backUp();
		}
		
		return rval;
	}
}