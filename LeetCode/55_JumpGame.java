// https://leetcode.com/problems/jump-game/description/?envType=study-plan&id=dynamic-programming-i
// 2023年03月03日 10:46:07

// 3ms
class Solution {
    public boolean canJump(int[] nums) {
        int mRI = nums[0]; // recording max reachable idx
        for (int i = 0; i < nums.length; i++) {
            if (i <= mRI) {
                nums[i] += i; // recording current reachable idx
                mRI = Math.max(nums[i], mRI); // update mRI
            } else {
                return false;
            }
        }
        return true;
    }
}

// 2ms
class Solution {
    public boolean canJump(int[] nums) {
        int mRI = nums[0]; // recording max reachable idx
        for (int i = 0; i < nums.length; i++) {
            if (i <= mRI) {
                nums[i] += i; // recording current reachable idx
                mRI = Math.max(nums[i], mRI); // update mRI
                if (mRI > nums.length) {
                    return true;
                }
            } else {
                return false;
            }
        }
        return true;
    }
}