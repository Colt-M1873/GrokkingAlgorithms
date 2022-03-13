//  https://leetcode.com/problems/two-sum/
// 2022 3.13
# include <vector>
#include<unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // // v1 hashmap two pass
        // unordered_map<int,int> m;
        // for(int i=0;i<nums.size();++i){
        //     m[nums[i]]=i;
        // }
        // vector<int>ret(2,0);
        // for(int i=0;i<nums.size();++i){
        //     ret[0]=i;
        //     if(m.find(target-nums[i])!=m.end()){
        //         if(m[target-nums[i]]==i) continue;
        //         ret[1]=m[target-nums[i]];
        //         return ret;
        //     }
        // }
        // return ret;
        
        // v1.1 copied hashmap one pass
        unordered_map<int,int> m;
        vector<int>ret(2,0);
        for(int i=0;i<nums.size();++i){
            if(m.find(target-nums[i])!=m.end()){
                if(m[target-nums[i]]==i) continue;
                ret={i,m[target-nums[i]]};
                return ret;
            }else{
                m[nums[i]]=i;
            }
        }
        return ret;
    }
};