import java.util.*;
import java.lang.Math;

public class MaxAmongTen
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int[] arr=new int[10];
			for(int i=0;i<10;i++)
			{
				arr[i]=s.nextInt();
			}
			int max=arr[0];
			for(int i=0;i<10;i++)
			{
				if(arr[i]>max)
					max=arr[i];
			}
			System.out.println(max);
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
