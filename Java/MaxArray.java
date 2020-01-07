import java.io.*;
import java.util.*;

public class MaxArray
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int n=s.nextInt();
			int[] arr=new int[n];
			for(int i=0;i<n;i++)
			{
				arr[i]=s.nextInt();
			}
			
			int max=0;
			for(int i=0;i<n;i++)
			{
				if (arr[i]>max)
				{
					max=arr[i];
				}
			}
			System.out.println(max);
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
