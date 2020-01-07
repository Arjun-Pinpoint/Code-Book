import java.io.*;
import java.util.*;

public class NAD
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int n,a,d;
			n=s.nextInt();
			a=s.nextInt();
			d=s.nextInt();
			
			int res=0;
			for(int i=0;i<n;i++)
			{
				int calc=a+(i*d);
				res+=calc;
			}
			System.out.println(res);
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
