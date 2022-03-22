// https://leetcode.com/problems/merge-sorted-array/
// 2022 3.14

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // v1 bubble sort, slow and dumb 
        if(nums2.begin()==nums2.end()) return ;
        
        for(int i=m;i<m+n;++i){
            nums1[i]=nums2[i-m];
        }
        for(int i=0;i<nums1.size();++i){
            cout<<nums1[i]<<", ";
        }
        cout<<endl;
        int tmp;
        int p1=0,p2=m;
        while(p1<m+n){
            for(p2=p1;p2<m+n;p2++){
                if(nums1[p1]>nums1[p2]){
                    tmp=nums1[p1];
                    nums1[p1]=nums1[p2];
                    nums1[p2]=tmp;
                }
            }
            p1++;
        }
        return ;
    }
};