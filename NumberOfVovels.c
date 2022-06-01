//Program to find number of vovels in string
#include<stdio.h>
#include<conio.h>

int main()
{
    int c = 0, check = 0;
    char s[1000];
    printf("Input a string\n");
    gets(s);
    while (s[c] != '\0') 
    {
        if (s[c] == 'a' || s[c] == 'A' || s[c] == 'e' || s[c] == 'E' || s[c] == 'i' || s[c] == 'I' || s[c] =='o' || s[c]=='O' || s[c] == 'u' || s[c] == 'U')
        check++;
        c++;
    }
    printf("Number of vowels in the string: %d", check);
    return 0;
}
