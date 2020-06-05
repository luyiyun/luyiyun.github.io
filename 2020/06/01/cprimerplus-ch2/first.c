#include <stdio.h>

int main(void)                  // int indicates that the func returns an integrer,
                                //   void indicates that the func doesn't take any arguments.
{
    int num;                    // define a variable called num
    num = 1;                    // assign a value to num

    printf("I am a simple ");   // use the printf() function
    printf("computer.\n");
    printf("My favorite number is %d because it is first.\n", num);

    retrun 0;                  // For the present, just regard this line as the appropriate closing for the func.
}