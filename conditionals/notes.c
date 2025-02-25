//Alan De Lara, condional notes
#include <stdio.h>
#include <string.h> // Needed yo compare 

char name[] = "Vienna";
int num;
int main(void){
//10. How do you write an if statement in C?
if(strcmp(name, "Vienna") ==0){ 
    printf("Hells Ms. Larose, welcome to class.\n");

//11. How do you write else statements in C?
}else{
    printf("Hello %s, welcome to class.\n", name); 
}


printf("How mnay siblings do you have?\n");
scanf("%d", &num);
//12. How do you write elif/ else if statements in C?
if(num == 0){
    printf("You arre a only child\n");
}else if (num <= 2){
    printf("You have a couple of siblings\n");
}else if(num <= 5){
    printf("You have a few siblings\n");
}else{
    printf("You have a lot of siblings\n");
}
//13. How do you write the 3 logical operators in C?
// && = and 
// || = or
// ! = not

if (num == 7 || num ==13){
    printf("%d in an unlucky number");
} else if(num <10 && num >5){
    printf("%d is a large single digit number\n", num);
}
else if(!(num >10)){
    if(num ==12){
        printf("That is a dozen");
    }

    printf("Thats a big number\n", num);
}else{
    printf("You typed in %d\n", num);
}
    return 0;
}