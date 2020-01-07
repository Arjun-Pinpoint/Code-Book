import java.util.*;
import java.lang.Math;

public class prime
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int n=s.nextInt();
			
			int f=0;
			for(int i=2;i<n-1;i++)
			{
				if(n%i==0)
				{
					f=1;
					break;
				}
			}
			if(f==0)
				System.out.println("yes");
			else
				System.out.println("no");
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
