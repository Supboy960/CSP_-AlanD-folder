// Alan De Lara, loops notes C
#include <stdio.h>



int main(void){
//1.What is a loop? 
    //A section of code repested multiple times
//2.What are the two types of loops?
    //while loops
    int start = 0;
    while(start <5){
        printf("Hello!\n");
        start++;
    }
    //For loops
    int q;
    for(q=0;q<5;q++){
        printf("%d\n",q);
    }
//3.What is iteration
    //Repeting something with minor changes each time

//4.What are arrays(lists)? 
    //an array (list) is a varibale holing multpie values

//8.How do you make arrays(lists) in C?
    //Array itmees must all be the same data type!
int grades[] = {88, 97, 100, 70, 72, 99, 61};
    // 1. set data type 2. AFTER naiming put vrackets and wirte the length of the list 3. list is surrounded by curly brackets{} 4. commas, between each item
//print a single item from a list
printf("CSP GRADE:%d\n", grades[2]);
//Change an item in the array
grades[2]= 95;
printf("CSP GRADE:%d\n", grades[2]);
//SIxe of array in bytes
int size = sizeof(grades);
//length in array items
int length = sizeof(grades)/sizeof(grades[0]);
printf("The array is %d items long.\n", length);
//Array with strings
//Farist brackets sets lenth of array
//Second brackets sets length of each string
char movies[][20] = {"Cars", "Treasure Planet", "An American Tale", "Marley and Me", "the Avengers"};
printf("The movie is %s!\n", movies[1]);
int mlength = sizeof(movies)/sizeof(movies[0]);
//9.How do you make for loops in C?
// set the iterator, keeps track of time through the loop (best practice to set as x or i)
int x;
//in parens (starting point; ending point; count by)
for(x=0; x<=10;x+=2){
    printf("%d\n", x);
}
int m;
for(m=0;m<mlength;m++){
    printf("%s\n", movies[m]);
}
//10.How do you make while loops in C?
    int w = 0;

    while(w<100){
        printf("%d\n", w);
        w += 10;
    }
    return 0;
}