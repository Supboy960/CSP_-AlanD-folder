//Alan De Lara, Family loops 

#include <stdio.h>  
  
int main() {  
    char* family_names[] = {"Eduardo", "Daysi", "Alan", "Melaine", "Aaron", "Melissa", "Mardilea"};  
      
    for (int i = 0; i < sizeof(family_names) / sizeof(family_names[0]); i++) {  
        printf("Hello %s\n", family_names[i]);  
    }  
      
    return 0;  
}  
