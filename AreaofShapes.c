//Program to find area of triangle rectangle circle
#include<stdio.h>
#include<conio.h>

void triangle(int l , int b)
{
    int at;
    at = (l*b)/2;
    printf("Area of triangle is : %d",at);
}
void rectangle(int l , int b)
{
    int at;
    at = l*b;
    printf("Area of triangle is : %d",at);
}
void circle(int r)
{
    int at;
    at = 3.14*r*r;
    printf("Area of triangle is : %d",at);
}

int main()
{
    int ch,l,b,r;
    printf("This is Area Calculator Program : ");
    printf("\nEnter Your Choice\n1.Triangle\n2.Rectangle\n3.Circle\n");
    scanf("%d",&ch);
    switch (ch)
    {
    case 1:
        printf("Enter base and height of triangle");
        scanf("%d%d",&l,&b);
        triangle(l,b);
        break;
    case 2:
        printf("Enter length and breadth of rectangle");
        scanf("%d%d",&l,&b);
        rectangle(l,b);
        break;
    case 3:
        printf("Enter redius of circle");
        scanf("%d",&r);
        circle(r);
        break;
    default:
        break;
    }
    return 0;
}