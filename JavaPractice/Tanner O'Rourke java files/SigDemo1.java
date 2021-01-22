import javax.swing.JOptionPane;

public class SigDemo1
{
	public static void main( String[] args )
	{
		testMe( 0 );
		testMe( "" );
	}
	private static void testMe( int param )
	{
		JOptionPane.showMessageDIalog( null, "hi im test me" );
	}
	
	private static void testMe( String param )
	{
		JOptionPane.showMessageDIalog( null, "hi im test me STRING" );
	}
}
	
	