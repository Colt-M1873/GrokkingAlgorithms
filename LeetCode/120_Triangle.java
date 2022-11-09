// https://leetcode.com/problems/triangle/
// 2022年11月09日 17:23:09
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        for (int i = 1; i < triangle.size(); i++) {
            int rowSize = triangle.get(i).size();
            triangle.get(i).set(0, triangle.get(i).get(0) + triangle.get(i - 1).get(0));
            for (int j = 1; j < rowSize - 1; j++) {
                int minOfLast2 = Math.min(triangle.get(i - 1).get(j - 1), triangle.get(i - 1).get(j));
                triangle.get(i).set(j, triangle.get(i).get(j) + minOfLast2);
            }
            triangle.get(i).set(rowSize - 1, triangle.get(i).get(rowSize - 1) + triangle.get(i - 1).get(rowSize - 2));
        }
        int minOfLastRow = triangle.get(triangle.size() - 1).get(0);
        for (int val : triangle.get(triangle.size() - 1)) {
            minOfLastRow = Math.min(minOfLastRow, val);
        }
        System.out.println(triangle);
        return minOfLastRow;
    }
}