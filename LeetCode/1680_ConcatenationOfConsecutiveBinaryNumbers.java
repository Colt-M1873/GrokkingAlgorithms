// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
// 2022年09月23日 15:34:19


// v0 correct but TLE, 
// a whole long string is inefficent
class Solution {
    public int concatenatedBinary(int n) {
        int M=1000000007;
        String str="";
        for(int i=1;i<=n;i++){
            str=str+Integer.toBinaryString(i);
        }
        // System.out.println(str);
        int ret=0;
        for(int j=0;j<str.length();j++){
            ret=(ret*2+(str.charAt(j)-'0'))%(M);
        }
        return ret;
    }
}


// v1 1067ms rlatively slow
class Solution {
    public int concatenatedBinary(int n) {
        int M=1000000007;
        String currStr="";
        int ret=0;
        for(int i=1;i<=n;i++){
            currStr=Integer.toBinaryString(i);
            // System.out.println(currStr);
            for(int j=0;j<currStr.length();j++){
                ret=(ret*2+(currStr.charAt(j)-'0'))%M;
            }
        }
        return ret;
    }
}