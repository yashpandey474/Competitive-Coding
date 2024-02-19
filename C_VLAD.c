#include <stdio.h>


int main(){
    int t;
    scanf("%d", &t);

    for (int test = 0; test < t; test += 1){
        int n;
        scanf("%d", &n);
        
        int result = 0;
        if (n % 10 == n){
            result = (n*(n + 1))/2;
            printf("%d\n", result);
        }

        else{
            while (n){
                result += (n % 10);
                n /= 10;
            }
            printf("%d\n", result);
        }
    }
}