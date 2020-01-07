import java.util.*;

public class SortArray
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
			for(int i=0;i<n;i++)
			{
				System.out.print(arr[i]+" ");
			}
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}
