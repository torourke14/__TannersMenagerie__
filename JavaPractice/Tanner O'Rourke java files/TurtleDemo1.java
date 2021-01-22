public class TurtleDemo1
{
	public static void main( String[] args)
	{
		Turtle dorothy = new Turtle();
		dorothy.paint( 45,128 ); // (angle pointing, pixels)
		dorothy.paint( -45,256 );
		dorothy.paint( -135,256 );
		dorothy.paint( -90,64 );
		dorothy.move ( -45,128 );
		dorothy.paint( -90,64 );
		dorothy.swingAround ( 64 );
	}
}