// https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
// 2023年03月03日 16:04:07

class Solution {
    public int search(int[] nums, int target) {
        int ret = 0;
        for (int n : nums) {
            if (n == target) {
                ret++;
            }
        }
        return ret;
    }
}