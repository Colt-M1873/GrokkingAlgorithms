// https://leetcode.com/problems/satisfiability-of-equality-equations/
// 2022年09月26日 20:44:18

// nice video about union find https://www.youtube.com/watch?v=KbFlZYCpONw&ab_channel=WilliamFiset
// v1 2ms, little bit slow, simpler version of union find
// union find without path compression
// because the deepest tree in this problem will have the 
// length of 26, i.e. the total alphabet, not too big,
// so the speed is not too slow without path compression 
class Solution {
    int[] id = new int[26];// denotes the index of 26 characters
    
    public Solution(){
       for (int i=0;i<id.length;i++){
            id[i]=i;
        }
    }
    
    public boolean equationsPossible(String[] equations) {
        char[] uf = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        for (String s: equations) {
            if (s.charAt(1)=='='){
                // union b into a
                int roota=find(s.charAt(0)-'a');
                int rootb=find(s.charAt(3)-'a');
                if (roota != rootb ){
                    id[roota]=rootb;
                }
            }
        }
        for (String s: equations) {
            if (s.charAt(1)=='!'){
                // union b into a
                if (find(s.charAt(0)-'a')==find(s.charAt(3)-'a')){
                    return false;
                }
            }
        }
        return true;
    }
    
    private int find(int idx){ // write find first, then think about union
        int root=idx;
        while (id[root]!=root){
            root=id[root];
        }
        // no path compression
        return root;        
    }
    
}

// v1.1 1ms, faster than 100%, union find with path compression
class Solution {
    int[] id = new int[26];// denotes the index of 26 characters
    
    public Solution(){
       for (int i=0;i<id.length;i++){
            id[i]=i;
        }
    }
    
    public boolean equationsPossible(String[] equations) {
        char[] uf = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        for (String s: equations) {
            if (s.charAt(1)=='='){
                // union b into a
                int roota=find(s.charAt(0)-'a');
                int rootb=find(s.charAt(3)-'a');
                if (roota != rootb ){
                    id[roota]=rootb;
                }
            }
        }
        for (String s: equations) {
            if (s.charAt(1)=='!'){
                // union b into a
                if (find(s.charAt(0)-'a')==find(s.charAt(3)-'a')){
                    return false;
                }
            }
        }
        return true;
    }
    
    private int find(int idx){ // write find first, then think about union
        int root=idx;
        while (id[root]!=root){
            root=id[root];
        }
        // path compression
        while (idx!=root){
            int nexttmp=id[idx];
            id[idx]=root; // directly connect to root
            idx=nexttmp;
        }
        return root;        
    }
    
}