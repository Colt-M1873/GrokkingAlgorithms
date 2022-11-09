// https://leetcode.com/problems/make-the-string-great/description/
// 2022年11月08日 16:51:04

class Solution {
    public String makeGood(String s) {
        StringBuilder sb=new StringBuilder();
        List<Character> l=new ArrayList<Character>();
        for(int i=0;i<s.length();i++){
            if(l.size()>=1 && (s.charAt(i)==l.get(l.size()-1)+32 || s.charAt(i)==l.get(l.size()-1)-32)){
                l.remove(l.size()-1);
            }else{
                l.add(s.charAt(i));
            }
        }
        for(char c:l){
            sb.append(c);
        }
        // System.out.println(l);
        return sb.toString();
    }
}