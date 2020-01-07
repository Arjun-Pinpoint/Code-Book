import java.util.*;
import java.lang.Math;

public class HourMin2
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int[] arr=new int[4];
			for(int i=0;i<4;i++)
			{
				arr[i]=s.nextInt();
			}
			int hour=Math.abs(arr[0]-arr[2]);
			int min=Math.abs(arr[1]-arr[3]);
			
			System.out.println(hour+" "+min);
			
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
