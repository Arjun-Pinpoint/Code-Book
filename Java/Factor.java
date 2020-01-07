import java.util.*;
import java.lang.Math;

public class Factor
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int n=s.nextInt();
			for(int i=1;i<n+1;i++)
			{
				if(n%i==0)
					System.out.print(i+" ");
			}
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
