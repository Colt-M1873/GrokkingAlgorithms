// https://leetcode.com/problems/valid-parentheses/
// 2022 3.13
# include <string>
# include <vector>
#include <unordered_map>
# include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        // v1 using stack
        unordered_map<char,char> m={{')','('}, {']','['}, {'}','{'}};
        vector<char>vc;
        for(int i=0;i<s.length();i++){
            if(vc.size()!=0 && m[s[i]]==vc.back()){
                vc.pop_back();
            }
            else{
                vc.push_back(s[i]);
            }            
        }
        return vc.size()==0;

        // v2 cpoied stack
        stack<char> paren;
        for (char& c : s) {
            switch (c) {
                case '(': 
                case '{': 
                case '[': paren.push(c); break;
                case ')': if (paren.empty() || paren.top()!='(') return false; else paren.pop(); break;
                case '}': if (paren.empty() || paren.top()!='{') return false; else paren.pop(); break;
                case ']': if (paren.empty() || paren.top()!='[') return false; else paren.pop(); break;
                default: ; // pass
            }
        }
        return paren.empty() ;

    }
};