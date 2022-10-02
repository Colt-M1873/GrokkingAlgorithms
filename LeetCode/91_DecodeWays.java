// https://leetcode.com/problems/decode-ways/
// 2022年10月01日 18:14:59

class Solution {
    public int numDecodings(String s) {
        int[] dp=new int[s.length()+1];
        // only 1 or 2 digits can be combined, like staircase, but with more constraints
        // move forward in two ways: 1 digit or two digits
        // when move by 1 digit, if currChar!='0' all case plus 1
        // when move by 2 digit, if charToNum not start with 0 and smaller than 27, all case plus 1
        // dp[i]=curr+dp[i-1] or curr+dp[i-2]
        dp[0]=1; // wtf why should dp[0] be 1????
        if(s.charAt(0)=='0'){return 0;}
        dp[1]=1;
        for (int i=1;i<s.length();i++) {
            if (s.charAt(i)!='0'){
                dp[i+1]+=dp[i];
            }
            if (s.charAt(i-1)!='0') {
                if(Integer.parseInt(s.substring(i-1,i+1)) <= 26){
                    // System.out.println(Integer.parseInt(s.substring(i-1,i+1)));
                    dp[i+1]+=dp[i-1];
                }
            }
            if (dp[i+1]==0){
                return 0;
            }
        }
        // for (int d:dp){
        //     System.out.print(d+",");
        // }
        // System.out.println();
        return dp[s.length()];
    }
}