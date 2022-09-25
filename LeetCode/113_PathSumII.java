// https://leetcode.com/problems/path-sum-ii/
// 2022年09月24日 12:23:38


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        // List<list<Integer>>  ret = new ArrayList<ArrayList<Integer>>();
        // List<Integer> path = new ArrayList<Integer>();
        return backTrack(root, targetSum, new ArrayList<Integer>() );
    }
    
    private List<List<Integer>> backTrack(TreeNode root, int targetSum, List<Integer> path) {
        List<List<Integer>>  ret = new ArrayList<List<Integer>>();
        if (root==null) { return ret; }
        path.add(root.val);
        if (root.left==null && root.right==null && root.val==targetSum){ 
            ret.add(new ArrayList<Integer>(path));// copy of path, dont directly use path
        }
        targetSum-=root.val;
        
        if (root.left!=null){
            ret.addAll(backTrack(root.left,targetSum,path));
            path.remove(path.size()-1);// because all path share the same memory
        }
        if (root.right!=null){
            ret.addAll(backTrack(root.right,targetSum,path));
            path.remove(path.size()-1);//          
        }
        return ret;
    }
    
}