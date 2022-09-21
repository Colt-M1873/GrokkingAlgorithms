// https://leetcode.com/problems/sort-array-by-parity-ii/
// 2022年09月21日 14:40:03


// v1 queue, slow, 9ms
class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        // record all misplaced odd elements
        Queue<Integer> qIdx = new LinkedList<>();
        for (int i=0;i<nums.length;i+=2){
            if (nums[i]%2==1){// if misplaced
                qIdx.offer(i);
            }
        }
        int idx,tmp;
        for (int i=1;i<nums.length;i+=2){
            if (nums[i]%2==0){// if misplaced
                idx=qIdx.poll();
                tmp=nums[i];
                nums[i]=nums[idx];
                nums[idx]=tmp;
            }
        }
        // System.out.print(qIdx.size());
        // System.out.print(qIdx);
        return nums;
    }
}



// v2 two pointer, fast 4ms
// https://leetcode.com/problems/sort-array-by-parity-ii/discuss/181160/Java-two-pointer-one-pass-inplace
class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int i=0, j=1, n=nums.length;
        while (i<n && j<n){
            while (i<n && nums[i]%2==0){
                i+=2;
            }
            while (j<n && nums[j]%2==1){
                j+=2;
            }
            if (i<n && j<n){
                swap(nums,i,j);
            }
        }
        return nums;
    }
    
    private void swap(int[] a, int i,int j){
        int tmp=a[i];
        a[i]=a[j];
        a[j]=tmp;
    }
    
}