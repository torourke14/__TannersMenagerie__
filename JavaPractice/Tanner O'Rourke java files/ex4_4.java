import javax.swing.JOptionPane;

public class BasicGame 
{
	private String secretWord_ = "duck" ;
	private String  usersGuess_ ;
	
	public void playOneGame()
	{
		askUsersFirstChoice();
		while ( shouldContinue() )
		{
			showUpdatedStatus();
			askUsersNextChoice();
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
		return rval;
	}
	
	public void showUpdatedStatus()
	{
		String message = "That was wrong. Hint: it quacks";
		JOptionPane.showMessageDialog( null, message );
	}
	
	public void showFinalStatus()
	{
		String message = "CONGRATS";
		JOptionPane.showMessageDialog( null, message );
	}
}