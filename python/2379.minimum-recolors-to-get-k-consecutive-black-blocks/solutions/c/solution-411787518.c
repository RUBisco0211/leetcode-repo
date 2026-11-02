// leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/  (2379)
// submission 411787518  accepted 2023-03-11  runtime 0 ms  memory 5.5 MB

int minimumRecolors(char* blocks, int k){
    int countW = 0;
    int min = k;
    for(int i=0;i+k<=strlen(blocks);i++){
        countW = 0;
        for(int j=0;j<k;j++){
            countW += blocks[i+j]=='W'?1:0;
        }
        min = min<countW?min:countW;
    }
    return min;
}
