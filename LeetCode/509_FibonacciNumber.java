// https://leetcode.com/problems/fibonacci-number/description/?envType=study-plan&id=dynamic-programming-i
// 2023年02月28日 16:58:40
class Solution {
    public int fib(int n) {
        if (n < 2) {
            return n;
        }
        int a = 0, b = 1, c = 1;
        for (int i = 1; i < n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
}

###### 2023年08月24日 14:37:08

class Solution {
    public int fib(int n) {
        // // recursive 6ms
        // if(n<2){return n;}
        // return fib(n-1)+fib(n-2);
        
        // dp 0ms
        if(n<2){return n;}
        int[] a = new int[n+1];
        a[1]=1;
        for(int i=2;i<n+1;i++){
            a[i]=a[i-1]+a[i-2];
        }
        return a[n];

        // O1 space dp
        if(n<2){return n;}
        int a,b,c;
        a=0;b=1;c=1;
        for(int i=2;i<n+1;i++){
            c=a+b;
            a=b;
            b=c;
        }
        return c;
    }
}

