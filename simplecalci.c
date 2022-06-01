// This is simple calculator program
#include<stdio.h>
#include<conio.h>

int main()
{
    int a,b,ch;
    printf("This is simple calculator");
    printf("\nEnter two numbers : ");
    scanf("%d%d",&a,&b);
    printf("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus");
    printf("\nNow Enter Your choice");
    scanf("%d",&ch);
    switch(ch)
    {
        case 1:
            printf("Addition Operation Selected :\nAddition of %d and %d = %d",a,b,a+b);
            break;
        case 2:
            printf("Subtraction Operation Selected :\nSubtraction of %d and %d = %d",a,b,a-b);
            break;
        case 3:
            printf("Multiplication Operation Selected :\nMultiplication of %d and %d = %d",a,b,a*b);
            break;
        case 4:
            printf("Division Operation Selected :\nDivision of %d and %d = %d",a,b,a*b);
            break;
        case 5:
            printf("Modulus Operation Selected :\nModulus of %d and %d = %d",a,b,a%b);
            break;
        default:
            printf("Wrong Option");
            break;
    }
    return 0;
}