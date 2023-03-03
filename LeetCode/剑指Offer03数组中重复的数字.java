// https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
// 2023年03月03日 16:01:18

class Solution {
    public int findRepeatNumber(int[] nums) {
        HashSet s = new HashSet<Integer>();
        for (int n : nums) {
            if (s.contains(n)) {
                return n;
            } else {
                s.add(n);
            }
        }
        return -1;
    }
}