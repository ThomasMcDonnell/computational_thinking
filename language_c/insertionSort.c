/*
 * & File   : insertionSort.c
 * Author   : Thomas McDonnell
 */

#include <stdio.h>

/* InsertionSort
 * The idea of this algorithm is to build your sorted array in place, 
 * shifting elements out of the way if necessary to make room as you go.
 *This algorithm has a running worst case of O(n**2), as the current  moves 
 *take O(n) and the swaps and comparisons also take O(n).
 */
 
 void insertionSort(int *arr, int len_arr)
{
    int start, left, current;   // initilize tracker variables 

    for (start = 1; start < len_arr; start++)
    {
        left = start - 1;
        current = arr[start];

        while (left >= 0 && arr[left] > current)    // is the element to the
        {                                          // left larger if so swap
            arr[left+1] = arr[left];
            left -= 1;  
        }
        arr[left+1] = current;  // move forward  
    }
}

/* 
 * Function for looping through and printing an array
 */
void printArray(int *arr, int len_arr)
{
    for (int i = 0; i < len_arr; i++)
    {
        printf("%d", arr[i]);
        printf("\n");
    }
}

int main(){
    int arr[10] = {90, 2, 343, 24, 55, 1, 0, 12, 13, 66};

    
    int len_arr = sizeof(arr)/sizeof(arr[0]); 
    printArray(arr, len_arr);
    insertionSort(arr, len_arr);
    printArray(arr, len_arr);
    

    return 0;
}
