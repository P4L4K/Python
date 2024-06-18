//to add 2 variables without using '+' and to multiply without using '*'
#include<iostream>
using namespace std;
int main()
{
  int a;
  cin>>a;
  int b;
  cin>>b;
  /*
  for (int i=0;i<a;i++)
  {
    b++;
  }
  cout<<"sum: "<<b;
  */
  int n=0;
  for (int i=0;i<a;i++)
  {
    n+=b;
  }
  cout<<"product: "<<n;
 
}