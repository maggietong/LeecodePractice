#include <stdio.h>

#define bool int
#define true 1
#define false 0

void sort(int[] nums, int length) {
    bool hasChange = true;
    int temp=0;
    for (int i=0; i<nums.length-1 && hasChang; i++) {
        hasChange = false;
        for (int j = 0; j < nums.length -1-i; j++) {
            if (nums[j] > nums[j + 1]) {
                temp = nums[j+1];
                nums[j+1]=nums[j];
                nums[j] = temp;
                hasChange = true;
            }
        }
    }
}


int main(void) {
    int nums[] = {5,32, 12, 57, 5, 18, 3};
    length = sizeof(nums)*sizeof(nums[0])
    sort(nums, length);
    for (int i=0; i<length; i++) {
        printf("%i", nums[i]);
        return 1;
    }
}


