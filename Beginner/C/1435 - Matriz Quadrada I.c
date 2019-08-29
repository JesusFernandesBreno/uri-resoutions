#include <stdio.h>


int main(){
    int n = 1;
    do {

            scanf("%i", &n);
            if (n == 0){
                break;
            }

            int m[n][n];

            int lmax = n-1;
            int lmin = 0;
            int num = 1;

            int i = 0;
            int j = 0;

            int k = n-(n/2);
            int l = 0;
            while (l < k) {
                while (i<n){
                    while (j<n){
                        if (((i >= lmin && i <= lmax) && (j >= lmin && j <= lmax))  && !((i >= (lmin+1) && i <= (lmax-1)) && (j >= (lmin+1) && j <= (lmax-1)))){
                            m[i][j] = num;
                        }
                        j += 1;
                    }
                    i += 1;
                    j = 0;
                }
                lmax -= 1;
                lmin += 1;
                num += 1;
                l += 1;
                i = 0;
                j = 0;
            }
            i = 0;
            j = 0;
            while (i<n){
                    while (j<n){
                       if(j==0)
                        printf("%3d",m[i][j]);
                    else printf(" %3d",m[i][j]);
                        j += 1;
                    }
                    printf("\n");
                    j = 0;
                    i += 1;
            }
            printf("\n");
    } while (n != 0);

    return 0;
}

