import java.util.*;

public class DataType
{
	public static void main(String args[])
	{
		Scanner s=new Scanner(System.in);
		if(s.hasNextInt() || s.hasNextFloat())
		{
			System.out.println("yes");
		}
		else
			System.out.println("No");

	}

}
