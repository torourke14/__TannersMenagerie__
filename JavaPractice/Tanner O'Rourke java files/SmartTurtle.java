public class SmartTurtle extends Turtle
{
	public void makeSmallSquare()
	{
		paint( 90,40 );
		paint( 90,40 );
		paint( 90,40 );
		paint( 90,40 );
		move ( 90,15 );
		move ( 90,15 );
		paint ( 0,10 );
		paint ( 270,10 );
		paint ( 270,10 );
		paint ( 270,10 );
	}
	public void makeBigSquare()
	{
		paint( 90,40 );
		paint( 90,40 );
		paint( 90,40 );
		paint( 90,40 );
	}
	public void makeHexagon()
	{
		paint ( 0,30 );
		paint ( 60,30 );
		paint ( 60,30 );
		paint ( 60,30 );
		paint ( 60,30 );
		paint ( 60,30 );
	}
	public void MakeThreeHexagons()
	{
		makeHexagon();
		move ( 180,30 );
		makeHexagon();
		move ( 60,30 );
		move ( 60,30 );
		move ( 60,30 );
		move ( 240,0 );
		makeHexagon();
	}
}