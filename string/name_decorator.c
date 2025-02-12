//Alan De Lara, Name Decorator.C

#include <stdio.h>
#include <string.h>

char subject[50];
char name[]= "";



int main(void){
printf("What is your name?\n");
char one[]= "(: (:";
char two[]= "World!";
char three[]= ":) :)";
printf("%s\n", one);
strcat(one,two);
printf("%s", one);
strcat(two, three);//can only be cat two thing at a time
printf("%s",three);
    return 0;
}