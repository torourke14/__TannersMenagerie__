public class ImportantPerson extends Person
{
	private String birthday;
	
	public ImportantPerson()
	{
		birthday = "none";
	}
	
	public ImportantPerson( String first, String last )
	{
		super( first, last );
		birthday = "none";
	}
	
	public void setName( String first, String last, String birthday )
	{
		setFirstName( first );
		setLastName( last );
		setBirthday( birthday );
	}
	
	public void setBirthday( String birthday )
	{
		birthday = birthday;
	}
	
	public String getBirthday()
	{
		return birthday;
	}
	
	public String toString()
	{
		String name = super.toString() + ": " + birthday;
		return name;
	}
}