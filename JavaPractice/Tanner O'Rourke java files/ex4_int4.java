//Works Well!
public class ex4_int4 extends Turtle
{
	public static void main( String[] args )
	{
		ex4_int4 tim = new ex4_int4();
		tim.fiveCircles();
	}
	private void fiveCircles()
	{
		for ( int inx = 60 ; inx <= 300 ; inx = inx + 60 )
			swingAround( inx );
	}
}