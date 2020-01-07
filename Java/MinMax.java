import java.util.*;
import java.lang.Math;

public class MinMax
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
			
			int min=arr[0];
			int max=arr[0];
			for(int i=0;i<n;i++)
			{
				if(arr[i]>max)
					max=arr[i];
				if(arr[i]<min)
					min=arr[i];
			}
			System.out.println(min+" "+max);
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
