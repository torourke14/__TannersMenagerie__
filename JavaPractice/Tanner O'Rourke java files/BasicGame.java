//Works well!
import javax.swing.JOptionPane;

public class BasicGame 
{
	private String secretWord_ = "a duck";	  
	private String usersGuess_ ;
	private String counter_ = "";
	
	public void playOneGame()
	{
		askUsersFirstChoice();
		while ( shouldContinue() )
		{
			showUpdatedStatus();
			askUsersNextChoice();
			while ( shouldContinue() )
			{
				showUpdatedStatus2();
				askUsersNextChoice();
				while ( shouldContinue() )
				{
					showUpdatedStatus3();
					askUsersNextChoice();
				}
			}
		}
		showFinalStatus();
	}
	
	public void playManyGames()
	{
		int again = 0;
		do
		{
			playOneGame();
			again = JOptionPane.showConfirmDialog( null, "Again?" );
		} while ( again == JOptionPane.YES_OPTION );
	}
	
	public void askUsersFirstChoice()
	{
		usersGuess_ =
			JOptionPane.showInputDialog( null, "Guess the secret word" );
	}
	
	public void askUsersNextChoice()
	{
		askUsersFirstChoice();
	}
	
	public boolean shouldContinue()
	{
		boolean rval = !secretWord_.equals( usersGuess_ );
		counter_ = counter_ + "x";
		if ( counter_.equals( "xxxxx" ) )
			rval = false;
		return rval;
	}
	
	public void showUpdatedStatus()
	{
		String message = "That was wrong. Hint: is not boats of gravy ";
		JOptionPane.showMessageDialog( null, message );
	}
	
	public void showUpdatedStatus2()
	{
		String message = "That was wrong. Hint: its not very small rocks ";
		JOptionPane.showMessageDialog( null, message );
	}
	
	public void showUpdatedStatus3()
	{
		String message = "That was wrong. Hint: its not churches ";
		JOptionPane.showMessageDialog( null, message );
	}
	
	public void showFinalStatus()
	{
		String message = "CONGRATS";
		JOptionPane.showMessageDialog( null, message );
	}
}