// https://leetcode.com/problems/fibonacci-number/description/?envType=study-plan&id=dynamic-programming-i
// 2023年02月28日 16:58:40
class Solution {
    public int fib(int n) {
        if (n < 2) {
            return n;
        }
        int a = 0, b = 1, c = 1;
        for (int i = 1; i < n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
}