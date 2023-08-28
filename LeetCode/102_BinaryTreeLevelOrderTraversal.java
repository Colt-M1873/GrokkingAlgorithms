// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
// 2023年08月28日 16:59:05

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
    public List<List<Integer>> levelOrder(TreeNode root) {
      // 2ms
        ArrayList<TreeNode> queue=new ArrayList<TreeNode>();
        List<Integer> levelQueue=new ArrayList<Integer>();
        queue.add(root);
        levelQueue.add(0);
        int currLevel=-1;
        List<List<Integer>> ret=new ArrayList<List<Integer>>();
        if(root==null){return ret;}
        List<Integer> levelList=new ArrayList<Integer>();
        while(queue.size()>0){
            TreeNode curr=queue.get(0);
            int newLevel=levelQueue.get(0);
            
            if(newLevel!=currLevel){
                currLevel=newLevel;
                ret.add(levelList);
                levelList=new ArrayList<Integer>();
            }

            levelList.add(curr.val);

            queue.remove(0);
            levelQueue.remove(0);

            if(curr.left!=null){
                queue.add(curr.left);
                levelQueue.add(currLevel+1);
            }
            if(curr.right!=null){
                queue.add(curr.right);
                levelQueue.add(currLevel+1);
            }
        }

        ret.add(levelList);
        ret.remove(0);
        return ret;

        // // 0ms  from  https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/33450/java-solution-with-a-queue-used/comments/32165
        // List<List<Integer>> res = new ArrayList<>();  
        // if (root == null) return res;  
        // Queue<TreeNode> queue = new LinkedList<>();  
        // queue.add(root);  
        // while (!queue.isEmpty()) {  
        //     List<Integer> level = new ArrayList<>();  
        //     int cnt = queue.size();  
        //     for (int i = 0; i < cnt; i++) {  
        //         TreeNode node = queue.poll();  
        //         level.add(node.val);  
        //         if (node.left != null) {  
        //             queue.add(node.left);  
        //         }
        //         if (node.right != null) {  
        //             queue.add(node.right);  
        //         }  
        //     }  
        //     res.add(level);   
        // }  
        // return res;





      
    }
}
