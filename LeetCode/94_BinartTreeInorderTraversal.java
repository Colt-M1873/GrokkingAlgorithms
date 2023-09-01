// https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/

// 2023年09月01日 10:15:23
// iterative best practise
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> s=new Stack<TreeNode>();
        List<Integer> ret=new ArrayList<Integer>();
        while(root!=null || !s.isEmpty()){
            while(root!=null){
                s.add(root);
                root=root.left;
            }
            root=s.pop();
            ret.add(root.val);
            root=root.right;
        }
        return ret;
    }
}

// recursive
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ret=new ArrayList<Integer>();
        if(root!=null){
            ret.addAll(inorderTraversal(root.left));
            ret.add(root.val);
            ret.addAll(inorderTraversal(root.right));
        }
        return ret;
    }
}
