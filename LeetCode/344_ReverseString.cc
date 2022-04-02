// https://leetcode.com/problems/reverse-string/
// 2022年04月01日 21:55:48

class Solution {
public:
    void reverseString(vector<char>& s) {
        int i=0,j=s.size()-1;
        char temp;
        while(j>i){
            temp=s[i];
            s[i]=s[j];
            s[j]=temp;
            i++;
            j--;
        }
        
    }
};
