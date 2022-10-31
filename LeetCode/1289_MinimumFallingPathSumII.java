// https://leetcode.cn/problems/minimum-falling-path-sum-ii/
// 2022年10月22日 11:29:11

class Solution {
    public int rowMin(int[] row) {
        int m = row[0];
        for (int x : row) {
            if (x < m) {
                m = x;
            }
        }
        return m;
    }

    public int rowMinEvadeIndex(int[] row, int evadeIndex) {
        int m;
        if (evadeIndex != 0) {
            m = row[0];
        } else {
            m = row[1];
        }
        for (int i = 0; i < row.length; i++) {
            if (i == evadeIndex) {
                continue;
            } else {
                if (row[i] < m) {
                    m = row[i];
                }
            }
        }
        return m;
    }

    public int minFallingPathSum(int[][] grid) {
        for (int i = 1; i < grid.length; i++) {
            int lastRowMin = rowMin(grid[i - 1]);
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i - 1][j] != lastRowMin) { // iff item in current column is not the minimum of last row.
                    // then use the minimum of last row to sum
                    grid[i][j] += lastRowMin;
                } else { // if last item of current column is the minimum of last row, then recalculate
                         // minimum with this item
                    grid[i][j] += rowMinEvadeIndex(grid[i - 1], j);
                }
            }
        }

        return rowMin(grid[grid.length - 1]);
    }
}