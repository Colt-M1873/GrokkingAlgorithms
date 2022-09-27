// https://leetcode.cn/problems/missing-two-lcci/
// 2022年09月26日 14:11:48

// v0 failed for nums bigger than 100
// , multiplication generates too big interger
class Solution {
    public int[] missingTwo(int[] nums) {
        // we can know a+b and a*b
        // avoid big integer multiply from 1 to n, we just use 
        // sum of squares from 1 to n: 1^2 + 2^2 + 3^2 + ... + n^2 = [n(n+1)(2n+1)] / 6
        int allsum=0,
            allmult=1,
            sum=0,
            mult=1,
            apb=0,
            amb=0,
            a2pb2=0;
        for (int n:nums){
            sum+=n;
            mult*=n;
        }
        for (int i=1;i<=nums.length+2;i++){
            allsum+=i;
            allmult*=i;
        }
        apb=allsum-sum; // a plus b
        // System.out.println(mult);
        
        amb=allmult/mult; // a multiply b

        // System.out.println(apb);
        // System.out.println(amb);
        // (a+b)^2=a^2+2ab+b^2
        // a^2+b^2=apb^2-2amb
        // a^2+(apb-a)^2=apb^2-2amb
        // a^2+apb^2-2*a*apb+a^2=apb^2-2amb
        // 2a^2-2*apb*a+2amb=0
        // a=(2apb+-sqrt(4*apb^2-16amb))/4
        // System.out.println((2*apb+Math.sqrt(4*apb*apb-16*amb))/4);
        // System.out.println((2*apb-Math.sqrt(4*apb*apb-16*amb))/4);
        return new int[] {(int)((2*apb+Math.sqrt(4*apb*apb-16*amb))/4),(int)((2*apb-Math.sqrt(4*apb*apb-16*amb))/4)};
    }
}


// v1 suqare sum
class Solution {
    public int[] missingTwo(int[] nums) {
        // we can know a+b and a^2+b^2
        // avoid big integer multiply from 1 to n, we just use 
        // sum of squares from 1 to n: 1^2 + 2^2 + 3^2 + ... + n^2 = [n(n+1)(2n+1)] / 6
        int allsum=0, allsuqare=0,
            sum=0, squaresum=0,
            apb=0, a2pb2=0;
        for (int n:nums){
            sum+=n;
            squaresum+=n*n;
        }
        for (int i=1;i<=nums.length+2;i++){
            allsum+=i;
            allsuqare+=i*i;
        }
        apb=allsum-sum; // a plus b
        a2pb2=allsuqare-squaresum; // a suqre plus b square
        // a^2+b^2=a2pb2
        // a^2+(apb-a)^2=a2pb2
        // a^2+apb^2-2*a*apb+a^2=a2pb2
        // 2a^2-2*apb*a+apb^2-a2pb2=0
        // a=(2apb+-sqrt(4*apb^2-4*2*(apb^2-a2pb2)))/4
        // a=(2apb+-sqrt(8*a2pb2-4*apb^2)))/4
        // System.out.println((2*apb+Math.sqrt(8*a2pb2-4*apb*apb))/4);
        return new int[] {(int)((2*apb+Math.sqrt(8*a2pb2-4*apb*apb))/4),
                (int)((2*apb-Math.sqrt(8*a2pb2-4*apb*apb))/4)};
    }
}