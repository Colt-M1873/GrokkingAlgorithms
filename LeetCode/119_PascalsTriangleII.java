// https://leetcode.cn/problems/pascals-triangle-ii
// 2022年11月09日 17:07:11
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> lastRow = new ArrayList<Integer>(Arrays.asList(1));
        if (rowIndex == 0) {
            return lastRow;
        }
        List<Integer> currRow = new ArrayList<Integer>(Arrays.asList(1, 1));
        for (int i = 2; i <= rowIndex; i++) {
            lastRow = currRow;
            currRow = new ArrayList<Integer>();
            currRow.add(1);
            for (int j = 1; j < i; j++) {
                currRow.add(lastRow.get(j - 1) + lastRow.get(j));
            }
            currRow.add(1);
        }
        return currRow;
    }
}