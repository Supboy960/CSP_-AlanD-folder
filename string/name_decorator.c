//Alan De Lara, Name Decorator.C

#include <stdio.h>

#include <string.h>

char subject[50];
char name[]= "Victoria";
char sentence[]= "the quick brown fox jumps over the lazy dog.";


int main(void){
   char one[]= "Hello";
char two[]= "World!";
char three[]= "Welcome to my program. ";
printf("%s\n", one);
strcat(one,two);
printf("%s\n", one);
strcat(three, one);//can only be cat two thing at a time
printf("%s",three);
    return 0;
}