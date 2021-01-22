public class Vic1

{
	public static void main( String[] args )
	{
	Vic.reset(args);
	Vic jane = new Vic();
	Vic sally = new Vic();
	
	jane.moveOn();
	jane.moveOn();
	sally.moveOn();
	jane.takeCD();
	sally.putCD();
	jane.moveOn();
	jane.backUp();
	}
}