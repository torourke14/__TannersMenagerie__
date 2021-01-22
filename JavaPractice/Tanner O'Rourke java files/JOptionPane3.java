//Works well!
import javax.swing.JOptionPane;

public class JOptionPane3
{
	public static void main( String[] args )
	{
		String text =
			JOptionPane.showInputDialog( null, 
										"That was a bad idea",
										"Dialog Title",
										JOptionPane.WARNING_MESSAGE
										);
			if ( text.equals( "no it wasnt" ) );
				text = "shut up";
			if ( text == null )
				text = "That wasn't very nice";
			else if ( text.equals( "" ) )
				text = "You forgot to answer thoooo";
			else
				;
			JOptionPane.showMessageDialog( null, text );
	}
}