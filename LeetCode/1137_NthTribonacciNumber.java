// https://leetcode.cn/problems/n-th-tribonacci-number/
// 2022年10月20日 20:26:38
class Solution {
    public int tribonacci(int n) {
        // v2 dp
        int[] a;
        if (n>2){
            a=new int[n+1];
        }else{
            a=new int[3];
        }
        a[0]=0; a[1]=1;a[2]=1;
        for (int i=3;i<n+1;i++){
            a[i]=a[i-1]+a[i-2]+a[i-3];
        }
        return a[n];
        // // v1 recursion TLE
        // if(n<2){return n;}
        // if(n==2){return 1;}
        // return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3);
    }
}