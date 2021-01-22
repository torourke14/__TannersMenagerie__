import javax.swing.JOptionPane;

public class SigDemo2Subclass extends SigDemo2
{
	public static void main( String[] args )
	{
		SigDemo2Subclass obj1 = new SigDemo2Subclass();
		JOptionPane.showMessageDialog( null, obj1.testMe1() );
		JOptionPane.showMessageDialog( null, obj1.testMe2() );
	}
	
	public String testMe2()
	{
		return "SigDemo2Subclass testMe 2";
	}
}