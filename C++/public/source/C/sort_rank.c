#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define SIZE 5
#define INT_MAX 2147483647

void seqSort(int array[]);

int main() {
    int arr[SIZE], sorted_arr[SIZE], rank[SIZE];
    printf("Input 5 integers: ");
    scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);
    
    for (int i = 0; i < SIZE; i++) {
        sorted_arr[i] = arr[i]; // Copy original array
    }

    seqSort(sorted_arr);

    int same_rank;
    for (int i = 0; i < SIZE; i++) { // Compare with sorted_arr and original_arr
        same_rank = 0;
        for (int j = 0; j < SIZE; j++) {
            if (sorted_arr[i] == arr[j]) {
                rank[j] = i + 1;
                same_rank++;
            }
        }
        i += (same_rank - 1);
    }

    for (int i = 0; i < SIZE; i++) {
        printf("%d=r%d ", arr[i], rank[i]); // Print Output
    }

    return 0;
}

void seqSort(int array[]) { // Sort algo (Sequential Sort)
    int temp;
    for (int i = 0; i < SIZE; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            if (array[i] < array[j]) {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}
