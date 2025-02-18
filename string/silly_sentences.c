//Alan De Lara, Silly Sentences - C
#include <stdio.h>
//empty string varibaes for users (Minum 3)
char name[50];
char location[50];
char time[50];
char vehicle[50];
char speed[50];
char color[50];
char animal[50];
int main(void){
    // A welcome for the user telling them what the progtagam is (pirint)
printf("Welcome user this is a Silly Sentence that will depend on what words you write.");
printf(" Note I will want you to type one word for each qestion I will ask. :)" );
printf(" What is your name: ");
scanf("%s", name);
printf("Hi %s", name);
printf(" What is the location you are at:");
scanf("%s",location );
printf("What time is it (Morning, afternoon, night):");
scanf("%s", time);
printf("What vehicle do you like:");
scanf("%s",vehicle);
printf("What speed do you like to travel at:");
scanf("%s", speed);
printf("What is your favorite color:");
scanf("%s", color);
printf("What is your favorite animal:");
scanf("%s", animal);
    //ASK USER FOR WORDS (PRINT STATEMENT WITHA QESTION SACN F TO SET TO VARIBALE) (ine c we need to tell user that they can oly tpye 1 word)

    //pint out the stor whit the varibales inserted (" weclome %s to may prgeam",  name) One print atament


printf("%s%s%s%s%s%s","It was ", time, " when the ", vehicle, " came to pick me up for ", location, " The ride was ", speed, " and along the way I saw a ",color, animal );
printf("%s","Hope you have a wonderful day and try this code agian,",name);
    return 0;
}