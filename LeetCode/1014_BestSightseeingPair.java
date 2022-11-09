// https://leetcode.cn/problems/best-sightseeing-pair
// 2022年11月09日 16:35:33
class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        // 假设我们已知前一个节点 j 能组成的最大的组合为（i，j）， 那么紧接着的一个节点 j+1
        // 最大得分的组合一定是（i，j+1）和（j，j+1）这两个组合中较大的一个。
        int a = 0, b = 1; // a,b as a pair of index
        int ret = values[b] + values[a] - (b - a);
        for (int i = 2; i < values.length; i++) {
            int newbPair = values[i] + values[a] - (i - a);
            int newaPair = values[b] + values[i] - (i - b);
            if (newbPair > newaPair) {
                b = i;
                ret = Math.max(newbPair, ret);
            } else {
                a = i;
                ret = Math.max(newaPair, ret);
            }
        }
        return ret;
    }
}