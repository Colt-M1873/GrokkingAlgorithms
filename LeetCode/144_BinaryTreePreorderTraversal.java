// https://leetcode.com/problems/binary-tree-preorder-traversal/description/

// 2023年08月31日 14:58:40
// recursive
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> curr=new LinkedList<Integer>();
        if(root==null) return curr;
        curr.add(root.val);
        curr.addAll(preorderTraversal(root.left));
        curr.addAll(preorderTraversal(root.right));
        return curr;
    }
}

// iterative
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> ret = new LinkedList<Integer>();
        stack.add(root);
        while(stack.size()>0){
            TreeNode curr=stack.pop();
            if(curr!=null){
                ret.add(curr.val);
                stack.add(curr.right);
                stack.add(curr.left);
            }
        }
        return ret;
    }
}
