// leetcode.cn/problems/convert-the-temperature/  (2469)
// submission 415766788  accepted 2023-03-21  runtime 0 ms  memory 5.4 MB

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize){
    double* temp = (double*)malloc(sizeof(double)*2);
    temp[0] = celsius + 273.15;
    temp[1] = celsius*1.80 + 32.00;
    *returnSize = 2;
    return temp;
}
