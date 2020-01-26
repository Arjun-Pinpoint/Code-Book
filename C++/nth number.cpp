#include<iostream>
using namespace std;
int main()
{
    int i, n, a=0, b=0;
    cout<<"enter number : ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
        if(i%2!=0)
        {
            a = a + 7;
        }
        else
        {
            b = b + 6;
        }
    }
    if(n%2!=0)
    {
        cout<<n<<" term of series is "<<a-7;
    }
    else
    {
        cout<<n<<" term of series is "<<b-6;
    }
    return 0;
}


