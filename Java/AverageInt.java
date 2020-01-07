import java.util.*;
import java.lang.Math;

public class AverageInt
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int n=s.nextInt();
			int[] arr=new int[n];
			for(int i=0;i<n;i++)
				arr[i]=s.nextInt();
			
			int total=0;
			for(int i=0;i<n;i++)
			{
				total+=arr[i];
			}
			
			System.out.println(total/n);
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
