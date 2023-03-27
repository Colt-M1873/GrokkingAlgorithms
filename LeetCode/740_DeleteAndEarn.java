// https://leetcode.com/problems/delete-and-earn/submissions/908240764/?envType=study-plan&id=dynamic-programming-i
// 2023年03月03日 17:13:38

class Solution {
    public int deleteAndEarn(int[] nums) {
        // house robber but treat hash table keys as houses, values as loot prices
        Map h = new HashMap<Integer, Integer>();
        HashSet s = new HashSet<Integer>();
        for (int n : nums) {
            if (h.containsKey(n)) {
                h.put(n, (int) h.get(n) + n);
            } else {
                h.put(n, n);
            }
            s.add(n);
        }
        int[] keyArr = new int[s.size()];
        int i = 0;
        for (Object ns : s) {
            keyArr[i] = (int) ns;
            i++;
        }
        Arrays.sort(keyArr); // sort to get a increasing sequence
        // house robber with condition that if two houses are adjacent
        int[] dp = new int[s.size()];
        dp[0] = (int) h.get(keyArr[0]);
        if (keyArr.length == 1) {
            return dp[0];
        }
        if (keyArr[0] == keyArr[1] - 1) {
            dp[1] = Math.max(dp[0], (int) h.get(keyArr[1]));
        } else {
            dp[1] = dp[0] + (int) h.get(keyArr[1]);
        }
        for (i = 2; i < keyArr.length; i++) {
            if (keyArr[i - 1] == keyArr[i] - 1) {
                dp[i] = Math.max(dp[i - 1], dp[i - 2] + (int) h.get(keyArr[i]));
            } else {
                dp[i] = dp[i - 1] + (int) h.get(keyArr[i]);
            }
        }
        return Math.max(dp[dp.length - 1], dp[dp.length - 2]);
    }
}