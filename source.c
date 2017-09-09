#include <stdio.h>

main(void)
{
        int a,i,z;
        int step = 10000;
        printf("Please input a 5 digit integer value: ");
        scanf("%d",&a);
        printf("You entered: %d\n",a);
        for(i = 0; i < 5; i++) {
                int temp = a/step;
                printf("%d\n",temp);
                a = a%step;
                step = step/10;
        }
}
