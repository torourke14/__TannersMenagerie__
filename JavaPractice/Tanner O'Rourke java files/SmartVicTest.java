public class SmartVicTest
{
	public static void main (String[] args)
	{
	Vic.reset( args );
	
	SmartVic tim = new SmartVic();
	tim.movetake();
	tim.movetake();
	tim.backput();
	tim.backput();
	}
}