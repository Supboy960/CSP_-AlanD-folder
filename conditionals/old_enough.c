//Alan De Lara, Old Enough - C
#include <stdio.h>
int age;
int main(void){
    printf("Welcome to my old enough program that tells you whether you are old enough to vote, drive, get a learners permit, and go to school. (Don't take the advice given seriously from this program, this only for entertainment purposes only.)\n");

    printf("What is your age (in years!):\n");
    scanf("%d", &age);
    if(age < 5){
        printf("You aren't old enough to go to school, 6you can't get your get your learner's permit, drive, or vote.\nHow are you running this program?\nHow can you even read this?!?\n");
    } else if(age >= 18){
        printf("You are old enough to vote, drive, get your learner's permit, and (should be) go to school.\n");
    } else if(age >=16){
        printf("You are old enough to drive. Hopefully you know what to do at a red light!...(SLAM THE GAS!!!!)\n");
    } else if(age>=15){
        printf("You are old enough to get your learner's permit. Exciting, but be careful!\n");
    } else{
        printf("You are old enough and should be going to school.\n");
    }


    return 0;
}