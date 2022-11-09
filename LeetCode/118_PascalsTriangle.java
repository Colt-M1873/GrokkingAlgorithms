// https://leetcode.com/problems/pascals-triangle/
// 2022年11月09日 16:58:34

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> t = new ArrayList<List<Integer>>();
        t.add(new ArrayList<Integer>(Arrays.asList(1)));
        ArrayList<Integer> line = new ArrayList<Integer>();
        for (int i = 1; i < numRows; i++) {
            // line.clear();// 会删除掉t中的内容，不行
            line = new ArrayList<Integer>();
            line.add(1);
            for (int j = 1; j < i; j++) {
                line.add(t.get(i - 1).get(j) + t.get(i - 1).get(j - 1));
            }
            line.add(1);
            t.add(line);
        }
        System.out.println(t);
        return t;
    }
}