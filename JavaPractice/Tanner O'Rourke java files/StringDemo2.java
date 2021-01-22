public class StringDemo2
{
	public static void main( String[] args )
	{
		String fred    ="See spot!!";
		String wilma   ="See spot run!";
		String betty   ="Run spot, run!";
		
		System.out.println( fred.equals ( wilma ) );
		System.out.println( wilma.equals ( betty ) );
		System.out.println( betty.equals( "Run spot, run!" ) );
	}
}