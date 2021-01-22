public class LooperTest
{
	public static void main( String[] args )
	{
		Vic.reset( args );
		Looper loopy = new Looper();
		//loopy.fillSlots();
		//loopy.clearSlotsToStack();
		//loopy.fillOddSlots();
		//loopy.fillEvenSlots();
		loopy.SeesAllEvensFilled();
	}
}