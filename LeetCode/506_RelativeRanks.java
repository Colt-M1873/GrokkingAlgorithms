// https://leetcode.com/problems/relative-ranks/
// 2022年09月21日 12:20:53

// v1 to slow 216ms
class Solution {
    public String[] findRelativeRanks(int[] score) {
        String[] s=new String[score.length];
        int[] sorted = Arrays.copyOf(score,score.length);
        Arrays.sort(sorted);
        reverse(sorted);
        for (int i=0;i<score.length;i++){
            for (int j=0;j<sorted.length;j++){
                if (sorted[j]==score[i]){
                    if (j==0){
                        s[i]="Gold Medal";
                    }else if (j==1){
                        s[i]="Silver Medal";
                    }else if (j==2){
                        s[i]="Bronze Medal";
                    }else{
                        s[i]=String.valueOf(j+1);
                    }
                }
            }
        }
        return s;
    }

    static void reverse(int[] a){
        int i,tmp,n=a.length;
        for (i=0;i<n/2;i++){
            tmp=a[i];
            a[i]=a[n-1-i];
            a[n-1-i]=tmp;
        }
    }    
}


// v2 binary

class Solution {
    public String[] findRelativeRanks(int[] score) {
        int len=score.length;
        String[] s=new String[score.length];
        int[] sorted = Arrays.copyOf(score,score.length);
        Arrays.sort(sorted);
        for (int i=0;i<score.length;i++){
            int idx = binSearch(sorted, score[i]);
            if (idx==len-1){
                s[i]="Gold Medal";
            }else if (idx==len-2){
                s[i]="Silver Medal";
            }else if (idx==len-3){
                s[i]="Bronze Medal";
            }else{
                s[i]=String.valueOf(len-idx);
            }
        }
        return s;
    }
        
    static int binSearch(int[] a, int target){
        // a should be an ascending array
        int l=0,r=a.length,mid=(l+r)/2;
        while (l<r){
            mid=(l+r)/2;
            if (target<a[mid]){
                r=mid-1;
            }else if (target>a[mid]){
                l=mid+1;
            }else{
                return mid;
            }
        }
        return l;
    }
    
}



// v3 copied, hashmap
// https://leetcode.com/problems/relative-ranks/discuss/98468/Easy-Java-Solution-Sorting.
// in the comment
public class Solution {
    public String[] findRelativeRanks(int[] nums) {
        int[] ranks = nums.clone(); 
        Arrays.sort(ranks);
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i<ranks.length; i++){
            map.put(ranks[i], nums.length-i);
        }
        String[] res = new String[nums.length];
        for(int i = 0; i<nums.length; i++){
            int rank = map.get(nums[i]);
            String rankStr = rank+"";
            if(rank==1) rankStr = "Gold Medal";
            else if(rank==2) rankStr = "Silver Medal";
            else if(rank==3) rankStr = "Bronze Medal";
            res[i] = rankStr; 
        }
        return res; 
    }
}



// v4 copied, Pritority queue
// https://leetcode.com/problems/relative-ranks/discuss/1194733/java-priority-queue-solution-o(nlogn)-91faster
class Solution {
    public String[] findRelativeRanks(int[] score) {
        
        int n = score.length;
        String[] res = new String[n];
        
        PriorityQueue<Integer> pq = 
            new PriorityQueue<>((a,b)->score[b]-score[a]);
        
        for(int i=0;i<n;i++){
            pq.add(i);
        }
        int i=1;
        while(!pq.isEmpty()){
            
            int idx = pq.poll();
            
            if(i>3){
                res[idx] = Integer.toString(i);
            }else if(i==1){
                res[idx] = "Gold Medal";
            }else if(i==2){
                res[idx] = "Silver Medal";
            }else if(i==3){
                res[idx] = "Bronze Medal";
            }
            i++;
        }
        
        return res;
        
    }
}