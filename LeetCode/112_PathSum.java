// https://leetcode.com/problems/path-sum/submissions/
// 2022年09月24日 11:31:57


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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null){
            return false;
        }
        if (root.left==null && root.right==null && root.val==targetSum){
            return true;
        }
        targetSum-=root.val;
        return hasPathSum(root.left,targetSum) || hasPathSum(root.right,targetSum);
        
    }
}

// ###### 2023年08月24日 14:50:31
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null){return false;}
        if(root.left==null && root.right==null & root.val==targetSum){return true;}
        return hasPathSum(root.left,targetSum-root.val)||hasPathSum(root.right,targetSum-root.val);
        }
}
    
