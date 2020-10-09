#include <stdio.h>
int main () {
	int b_arr[10] = {31, -41, 59, 26, -53, 58, 97, -93, -23, 84};
	int i, j, max = 0,sum=0, n=10;
	for (i=0; i<n; i++) {
		sum = 0;
		printf("i is %d\n", i);
		for (j=i; j<n; j++) {
				sum += b_arr[j];
			printf("j: %d s: %d\n", j, sum);
			if (sum >= max){
				max = sum;
			}
		}
		}
	printf("%d", max);
}