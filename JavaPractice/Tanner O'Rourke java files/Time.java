public class Time
{
	private int hour_;
	private int min_;
	
	public Time( Time time )
	{
		hour_ = time.hour_;
		min_ = time.min_;
	}
	
	public Time add( Time toAdd )
	{
		int newHour = this.hour_ + toAdd.hour_;
		int newMin = this.min_ + toAdd.min_;
		
		Time result = new Time( newHour, newMin );
		return result;
	}
	
	public Time( int hour, int min )
	{
		hour_ = hour;
		
		for ( min_ = min ; min_ < 0 ; min_ = min_ + 60 )
			hour_--;
	}
	
	// overriding toString in Object class
	public String toString()
	{
	String time = "" + hour_ + min_;
	if ( hour_ < 10 )
		time = "0" + time;
	
	return time;
	}
}