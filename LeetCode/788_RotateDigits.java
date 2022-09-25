// https://leetcode.cn/problems/rotated-digits/
// 2022年09月25日 19:25:27

// v1 too slow
class Solution {
    public int rotatedDigits(int n) {
        int goodCount=0;
        for (int num=1;num<=n;num++){
            goodCount+=isGoodNumber(num);
        }
        return goodCount;
    }

    private int isGoodNumber(int origNum){
        // good number = must not include 347, must include 2569
        // not rotateable  3 4 7
        // the same after rotate 0 1 8
        // rotateable 2 5 6 9
        int currDigit,rotCount=0; // count rotateable digits
        Set<Integer> rot = new HashSet<>(Arrays.asList(2,5,6,9));
        Set<Integer> not = new HashSet<>(Arrays.asList(3,4,7));
        while (origNum>0) {
            currDigit=origNum%10;
            if( rot.contains(currDigit)){
                rotCount++;
            }else if(not.contains(currDigit)){
                return 0;
            }
            origNum=(int)Math.floor(origNum/10);
        }
        if (rotCount>0){return 1;}
        return 0;
    }
}



// v2 still slow
class Solution {
    public int rotatedDigits(int n) {
        int goodCount=0;
        for (int num=1;num<=n;num++){
            goodCount+=isGoodNumber(num);
        }
        return goodCount;
    }

    private int isGoodNumber(int origNum){
        // good number = must not include 347, must include 2569
        // not rotateable  3 4 7
        // the same after rotate 0 1 8
        // rotateable 2 5 6 9
        int rotCount=0; // count rotateable digits
        String s=Integer.toString(origNum);
        Character c;
        Set<Character> rot = new HashSet<>(Arrays.asList('2','5','6','9'));
        Set<Character> not = new HashSet<>(Arrays.asList('3','4','7'));
        for (int i=0;i<s.length();i++){
            c=s.charAt(i);
            if( rot.contains(c)){
                rotCount++;
            }else if(not.contains(c)){
                return 0;
            }
        }
        if (rotCount>0){return 1;}
        return 0;
    }
}


// v3 digit DP, superfast, 0ms   数位DP
// https://www.geeksforgeeks.org/digit-dp-introduction/
// https://leetcode.cn/problems/rotated-digits/solution/by-endlesscheng-9b96/
// https://mp.weixin.qq.com/s/8Z7W4xVnKLL3fLpjN6zXXQ
class Solution {
    static int[] DIFFS = {0, 0, 1, -1, -1, 1, 1, -1, 0, 1};

    char s[];
    int dp[][];

    public int rotatedDigits(int n) {
        s = Integer.toString(n).toCharArray();
        var m = s.length;
        dp = new int[m][2];
        for (var i = 0; i < m; i++) Arrays.fill(dp[i], -1);
        return f(0, 0, true);
    }

    int f(int i, int hasDiff, boolean isLimit) {
        if (i == s.length) return hasDiff; // 只有包含 2/5/6/9 才算一个好数
        if (!isLimit && dp[i][hasDiff] >= 0) return dp[i][hasDiff];
        var res = 0;
        var up = isLimit ? s[i] - '0' : 9;
        for (var d = 0; d <= up; ++d) // 枚举要填入的数字 d
            if (DIFFS[d] != -1) // d 不是 3/4/7
                res += f(i + 1, hasDiff | DIFFS[d], isLimit && d == up);
        if (!isLimit) dp[i][hasDiff] = res;
        return res;
    }
}