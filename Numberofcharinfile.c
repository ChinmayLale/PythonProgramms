//program to count number of char in files
#include<stdio.h>
#include<conio.h>
void main() 
{
	char ch;
	int count=0;
	FILE *fptr;
	fptr=fopen("hello.txt","r");
	if(fptr==NULL) 
    {
		printf("File can't be created\a");
		getch();
		exit(0);
	}
	while((ch=fgetc(fptr))!=EOF)
    {
		count++;
		printf("%c",ch);
	}
	fclose(fptr);
	printf("\nThe number of characters present in file is: %d",count);
}