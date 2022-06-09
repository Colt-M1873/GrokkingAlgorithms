//  https://leetcode.com/problems/add-strings/
// 2022 3.23

#include<iostream>

using namespace std;

class Solution {
public:
    string addStrings(string num1, string num2) {
        if(num1.length()<8 and num2.length()<8)
            return to_string(stoi(num1)+stoi(num2));
        int a,b,c=0,i,j;
        string result="";
        i=num1.length()-1;
        j=num2.length()-1;
        while(i>=0 or j>=0){
            a=(i>=0) ? num1[i]-'0' : 0;
            i--;
            b=(j>=0) ? num2[j]-'0' : 0;
            j--;
            result.insert(0,to_string((a+b+c)%10));
            c=(a+b+c)/10;
            // cout<<result<<endl;
            // cout<<a<<" "<<b<<" "<<c<<endl;
        }
        if(c==1)
            result.insert(0,to_string(c));
        return result;            
    }
};