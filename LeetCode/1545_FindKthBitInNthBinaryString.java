// https://leetcode.cn/problems/find-kth-bit-in-nth-binary-string/
// 2022年09月22日 17:09:40


//  v1 130ms
class Solution {
    public char findKthBit(int n, int k) {
        // cannot use int or long because the result may be way more than 64 bit
        // using array or sting instead
        ArrayList<Integer> arr = new ArrayList<Integer>();
        ArrayList<Integer> rev_arr = new ArrayList<Integer>();
        arr.add(0);
        rev_arr.add(1);
        for (int a=0;a<n-1;a++){
            arr.add(1);
            for (int i=rev_arr.size()-1;i>=0;i--){
                arr.add(rev_arr.get(i));
            }
            for (int j=rev_arr.size();j<arr.size();j++){
                rev_arr.add(arr.get(j)==1 ? 0 : 1 );
            }
            // System.out.println(arr);
        }
        return Character.forDigit(arr.get(k-1),10);
    }
}


//   v1.1 90ms
class Solution {
    public char findKthBit(int n, int k) {
        // cannot use int or long because the result may be way more than 64 bit
        // using array or sting instead
        ArrayList<Integer> arr = new ArrayList<Integer>();
        ArrayList<Integer> rev_arr = new ArrayList<Integer>();
        arr.add(0);
        rev_arr.add(1);
        for (int a=0;a<n-1;a++){
            arr.add(1);
            for (int i=rev_arr.size()-1;i>=0;i--){
                arr.add(rev_arr.get(i));
            }
            if (a==n-2){break;}
            for (int j=rev_arr.size();j<arr.size();j++){
                rev_arr.add(arr.get(j)==1 ? 0 : 1 );
            }
            // System.out.println(arr);
        }
        return Character.forDigit(arr.get(k-1),10);
    }
}