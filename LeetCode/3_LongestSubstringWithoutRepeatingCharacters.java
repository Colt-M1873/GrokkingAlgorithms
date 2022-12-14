// https://leetcode.cn/problems/longest-substring-without-repeating-characters/
// 2022年11月15日 14:42:36

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ret = 0;
        int l = 0, r = 1;// [)
        Map<Character, Integer> m = new HashMap<>();
        if (s.length() <= 1) {
            return s.length();
        }
        m.put(s.charAt(l), 1);
        while (r < s.length()) {
            if (!m.containsKey(s.charAt(r))) {
                m.put(s.charAt(r), 1);
                ret = Math.max(ret, m.size());
                r++;
            } else {
                while (l < r && m.containsKey(s.charAt(r))) {
                    m.remove(s.charAt(l));
                    l++;
                }
            }
        }
        return ret;
    }
}