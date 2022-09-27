// https://leetcode.cn/problems/check-permutation-lcci/
// 2022年09月27日 22:28:34

// v1 using hashmap
class Solution {
    public boolean CheckPermutation(String s1, String s2) {
        if (s1.length()!=s2.length()){return false;}
        Map<Character, Integer> d = new HashMap<Character, Integer>();
        // add char from s1 to hashmap
        for (int i=0;i<s1.length();i++){
            if (d.containsKey(s1.charAt(i))){
                int count=d.get(s1.charAt(i));
                d.put(s1.charAt(i),count+1);
            }
            else{
                d.put(s1.charAt(i),1);
            }
        }
        // delete char from hashmap according to s2
        for (int i=0;i<s2.length();i++){
            if (d.containsKey(s2.charAt(i))){
                int count=d.get(s2.charAt(i));
                if (count>1){
                    d.put(s2.charAt(i),count-1);
                }else{
                    d.remove(s2.charAt(i));
                }
            }
            else{
                return false;
            }
        }
        return d.size()==0;
    }
}


// v2 copied 
class Solution {
    public boolean CheckPermutation(String s1, String s2) {
        int n = s1.length(), m = s2.length(), tot = 0;
        if (n != m) return false;
        int[] cnts = new int[256];
        for (int i = 0; i < n; i++) {
            if (++cnts[s1.charAt(i)] == 1) tot++;
            if (--cnts[s2.charAt(i)] == 0) tot--;
        }
        return tot == 0;
    }
}
