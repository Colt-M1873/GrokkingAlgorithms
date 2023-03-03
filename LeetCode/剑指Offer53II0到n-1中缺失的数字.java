// https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
// 2023年03月03日 16:14:32
class Solution {
    public int missingNumber(int[] nums) {
        int ret = 0;
        for (int n : nums) {
            if (n != ret) {
                return ret;
            }
            ret++;
        }
        return ret;
    }
}