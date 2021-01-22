//Works well!
import javax.swing.JOptionPane;

public class ex4_1
{
	public static void main( String[] args )
	{
		String str1 =
			JOptionPane.showInputDialog( null, "I want two similar strings" );
		String str2 = 
			JOptionPane.showInputDialog( null, "Enter another string" );
			
		if ( str1 == null || str2 == null )
			System.out.println( "stop that!" );
		else if ( str1.equals( str2 ) )
			System.out.println( "String are equal" );
		else
			System.out.println( "one string is different from the other" );
			
	}
}