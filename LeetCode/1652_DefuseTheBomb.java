// https://leetcode.cn/problems/defuse-the-bomb/
// 2022年09月24日 11:16:08

class Solution {
    public int[] decrypt(int[] code, int k) {
        int[] ret=new int[code.length]; 
        // System.out.println((-2)%5);
        if(k==0){return ret;}
        for (int i=0;i<code.length;i++){
            // System.out.println(ret[i]);
            if(k>0){
                for (int j=i+1;j<=i+k;j++){
                    ret[i]+=code[j%code.length];
                }
            }else{
                for (int j=i-1;j>=i+k;j--){
                    ret[i]+=code[(code.length+j)%code.length];
                }
            }
        }
        return ret;
    }
}

// simplified
class Solution {
    public int[] decrypt(int[] code, int k) {
        int len = code.length;        
        int ans [] = new int[len];        
        int e = k >= 0 ? k == 0 ? 0 : 1 : -1;  //e取值为：[0,1,-1]
        for(int i = 0; i < len; i++){
            int sum = 0;
            for(int j = e; j != k + e; j += e){                
                sum += code[(i + j + len) % len];
            }
            ans[i] = sum;
        }
        return ans;
    }
}