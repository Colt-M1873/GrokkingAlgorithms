// https://leetcode.cn/problems/ti-huan-kong-ge-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
// 6ms
class Solution {
    public String replaceSpace(String s) {
        String ret = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                ret += "%20";
            } else {
                ret += s.charAt(i);
            }
        }
        return ret;
    }
}

// 0ms
class Solution {
    public String replaceSpace(String s) {
        return s.replace(" ", "%20");
    }
}