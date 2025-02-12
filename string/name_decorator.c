//Alan De Lara, Name Decorator.C

#include <stdio.h>    
#include <string.h>    
    
int main(void) {    
    char name[50];   
    
    printf("Welcome to the Name Decorator! This program will add text decorations on both sides of your name.\n");    
    printf("What is your name: ");    
    fgets(name, sizeof(name), stdin);    
    name[strcspn(name, "\n")] = 0;     
    
    printf("Hi %s\n", name);    
    
    char one[100] = "(: (: ";   
    char two[] = " :) :)";    
    strcat(one,name);
    strcat(one,two);
   printf(one);
    return 0;    
}  
