public class TimeTest
{
	public static void main( String[] args )
	{
		Time time1 = new Time( 13, 30 );
		System.out.println( time1.toString() );
		
		Time time2 = new Time( 12, 45 );
		System.out.println( time2.toString() );
		
		Time time3 = add( time2 );
		System.out.println( time3.toString() );
		
		Time time4 = time1.add( time2 );
		System.out.println( time4.toString() );
		
		
		
		
	}
}