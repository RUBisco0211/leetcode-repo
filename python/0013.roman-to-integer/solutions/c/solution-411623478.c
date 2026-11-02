// leetcode.cn/problems/roman-to-integer/  (13)
// submission 411623478  accepted 2023-03-10  runtime 12 ms  memory 5.9 MB

int romanToInt(char * s){
    int num = 0;
    int a[16];
    for(int i=0;i<strlen(s);i++){
        switch(s[i]){
            case 'I':a[i] = 1;break;
            case 'V':a[i] = 5;break;
            case 'X':a[i] = 10;break;
            case 'L':a[i] = 50;break;
            case 'C':a[i] = 100;break;
            case 'D':a[i] = 500;break;
            case 'M':a[i] = 1000;break;
        }
    }
    for(int i=1;i<strlen(s);i++){
        if(a[i]>a[i-1]){
            num -= a[i-1];
        }
        else{
            num += a[i-1];
        }
    }
    num += a[strlen(s)-1];
    return num;
}
