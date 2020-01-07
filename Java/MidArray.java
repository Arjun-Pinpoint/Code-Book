import java.util.*;

public class MidArray
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
			
			Arrays.sort(arr); //to sort an array
			
			int mid=n/2;
			System.out.println(arr[mid]);
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
