#include<stdio.h>
//for cpu bound : infinite program , end using ctrl + c
long long fact(int n)
{      
       if(n<1){
               return 1;}
       else if(n>1){
               return (n*(fact(n-1)));}
}

int main()
{
        int n=20;
        while(n>9)
        {

            printf("factorial of %d :%lld\n",n,fact(n));
            n--;
        }

}