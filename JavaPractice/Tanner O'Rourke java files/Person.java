//Works well!
public class Person
{
	private String firstName;
	private String lastName;
	
	public Person()
	{
		firstName = "none";
		lastName = "none";
	}
	
	public Person( String first, String last )
	{
		firstName = first;
		lastName = last;
	}
	
	public String getFirstName()
	{
		return firstName;
	}
	
	public void setFirstName( String name )
	{
		firstName = name;
	}
	
	public String toString()
	{
			String name = lastName + ", " + firstName;
			return name;
	}
}