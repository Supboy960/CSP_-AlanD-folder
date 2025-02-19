//Alan De Lara. Funtion Notes
#include <stdio.h>
int num;
char name[50], place[50], verb[50];
int add(int numOne, int numTwo){
     return numOne+numTwo;
}
void due(char assigment[50], char day[20]){
    printf("the %s assigmnet is due %s\n", assigment, day);
}
int main(void){
    //printf("Please tell me a number:\n");
    //scanf("%d", num);
    //add(num,10);
    //add(8,1);
    //add(4,85);
due ("funtions notes, Today");
due ("Hello world Update,  due tommorow");
due ("fanceil caltor Update, due friday");

    return 0;
}