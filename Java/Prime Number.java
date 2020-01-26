import java.util.Scanner;
class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        //input a number from user
        System.out.print("Enter the number to be checked : ");
        int n = sc.nextInt();
        //create object of class CheckPrime
        Main ob=new Main();
        //calling function with value n, as parameter
        ob.check(n);
        
    }
    //function for checking number is positive or negative 
    void check(int n)
    {
        if(n<0)
            System.out.println("Please enter a positive integer");
        else
            prime(n);
    }
    //function for checking number is prime or not 
    void prime(int n)
    {
        int c=0;
        for(int i=2;i<n;i++)
        {
            if(n%i==0)
            ++c;
            
        }
        if(c>=1)
            System.out.println("Entered number is not a prime number");
        else
            System.out.println("Entered number is a prime number");
    }
}


