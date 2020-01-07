import java.util.*;
import java.lang.Math;

public class Sum
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			int[] arr=new int[2];
			for(int i=0;i<2;i++)
				arr[i]=s.nextInt();
			
			System.out.println(arr[0]+arr[1]);
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
