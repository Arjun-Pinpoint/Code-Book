import java.util.*;
import java.lang.Math;

public class fibonacci
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int n=s.nextInt();
			
			int x=1;
			int y=1;
			System.out.print(x);
			
			for(int i=1;i<n;i++)
			{
				System.out.println(" ");
				int temp=y;
				System.out.print(y);
				y=y+x;
				x=temp;
				
			}
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
