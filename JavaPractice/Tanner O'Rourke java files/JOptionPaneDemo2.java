import javax.swing.JOptionPane;

public class JOptionPaneDemo2
{
	public static void main( String[] args )
	{
		String text =
			JOptionPane.showInputDialog( null, "Enter your name" );
		if ( text != null )
			System.out.println( "Your name is:" + text );
		else
			System.out.println( "you didnt input anything :-(" );
		
	}
}