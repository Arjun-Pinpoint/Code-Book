import java.util.*;

public class HourMin
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int sec=s.nextInt();
			
			int hour=sec/60;
			int min=sec%60;
			System.out.println(hour+" "+min);
			
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
