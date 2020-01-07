import java.util.*;
import java.lang.Math;

public class CheckInArray
{
	public static void main(String args[])
	{
		try
		{
			Scanner s=new Scanner(System.in);
			
			int[] arr1=new int[2];
			for(int i=0;i<2;i++)
			{
				arr1[i]=s.nextInt();
			}
			
			int[] arr2=new int[arr1[0]];
			for(int i=0;i<arr1[0];i++)
			{
				arr2[i]=s.nextInt();
			}
			
			int f=0;
			for(int i=0;i<arr1[0];i++)
			{
				if (arr2[i]==arr1[1])
				{
					f=1;
					break;
				}
			}
			if(f==1)
				System.out.println("yes");
			else
				System.out.println("no");
			
		}
		catch(Exception e)
		{
			System.out.println("Invalid Input");
		}

	}

}	
