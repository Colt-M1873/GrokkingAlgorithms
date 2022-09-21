// https://leetcode.com/problems/third-maximum-number/submissions/
// 2022年09月21日 15:12:27


// v1 soritng, slow, 237ms
class Solution {
    public int thirdMax(int[] nums) {
        bubbleSort(nums);
        int distinctCount=0;
        for (int i=1;i<nums.length;i++){
            if (nums[i]!=nums[i-1]){
                distinctCount++;
            }
            if (distinctCount==2){
                return nums[i];
            }
        }
        return nums[0];
        
    }
    
    private void bubbleSort(int[] nums){
        int tmp,n=nums.length;
        for (int i=0;i<n;i++){
            for (int j=i+1;j<n;j++){
                if (nums[i]<nums[j]) {
                    tmp=nums[i];
                    nums[i]=nums[j];
                    nums[j]=tmp;
                }
            }
        }
    }
    
}


// v1.1 quick sort 30ms
// quick sort using index as pivot
class Solution {
    public int thirdMax(int[] nums) {
        // bubbleSort(nums);
        quickSort(nums,0,nums.length-1);
        // System.out.print("\n");
        // for (int n:nums){
        //     System.out.print(n+",");
        // }
        int distinctCount=0;
        for (int i=1;i<nums.length;i++){
            if (nums[i]!=nums[i-1]){
                distinctCount++;
            }
            if (distinctCount==2){
                return nums[i];
            }
        }
        return nums[0];
    }
    
    
    
    private void quickSort(int[] arr, int left, int right){
        if (left<right){
            int pivot=partition(arr,left,right);
            quickSort(arr,left,pivot-1);
            quickSort(arr,pivot+1,right);
        }
    }
    private int partition(int[] arr, int left, int right){
        int pivot=left;
        int idx=pivot+1;
        for (int i=left+1;i<=right;i++){
            if (arr[i]>arr[pivot]){
                swap(arr,i,idx);
                idx++;
            }
        }
        swap(arr,pivot,idx-1);
        return idx-1;
    }
    
    private void swap(int[] arr, int i, int j){
        int tmp=arr[i];
        arr[i]=arr[j];
        arr[j]=tmp;
    }
    
}




// v1.3  real quick sort, 2ms
// quick sort using value as pivot and two pointer
class Solution {
    public int thirdMax(int[] nums) {
        quickSort(nums,0,nums.length-1);
        // System.out.print("\n");
        // for (int n:nums){
        //     System.out.print(n+",");
        // }
        int distinctCount=0;
        for (int i=1;i<nums.length;i++){
            if (nums[i]!=nums[i-1]){
                distinctCount++;
            }
            if (distinctCount==2){
                return nums[i];
            }
        }
        return nums[0];
    }
    
    
    private void quickSort(int[] arr, int left, int right){
        if (left<right){
            int pivot=partition(arr,left,right);
            quickSort(arr,left,pivot-1);
            quickSort(arr,pivot,right);
        }
    }
    private int partition(int[] arr, int left, int right){
        int pivot=arr[(left+right)/2];
        while (left<=right){
            while (arr[left]>pivot){
                left++;
            }
            while (arr[right]<pivot){
                right--;
            }
            if (left<=right){
                swap(arr,left,right);
                left++;
                right--;
            }
        }        
        return left;
    }
    
    private void swap(int[] arr, int i, int j){
        int tmp=arr[i];
        arr[i]=arr[j];
        arr[j]=tmp;
    }
    
 
}






// v2 prioroty queue, 19ms
// https://leetcode.com/problems/third-maximum-number/discuss/90190/Java-PriorityQueue-O(n)-%2B-O(1)
public class Solution {
    public int thirdMax(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            if (!set.contains(i)) {
                pq.offer(i);
                set.add(i);
                if (pq.size() > 3) {
                    set.remove(pq.poll());
                }
            }
        }
        if (pq.size() < 3) {
            while (pq.size() > 1) {
                pq.poll();
            }
        }
        return pq.peek();
    }
}


