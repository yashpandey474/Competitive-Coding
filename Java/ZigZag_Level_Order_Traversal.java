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

class Pair{
    TreeNode node;
    int level;

    Pair(TreeNode node, int level){
        this.node = node;
        this.level = level;
    }
}

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> lis = new ArrayList<>();
        List<Integer> arr = new ArrayList<>();
        Stack<TreeNode> stack1 = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();
        int prev_level = 0;
        TreeNode current;

        stack1.push(root);

        if(root == null){
            return lis;
        }

        while(!stack1.isEmpty() || !stack2.isEmpty()){
            if(!stack1.isEmpty()){
                arr = new ArrayList<>();
                while(!stack1.isEmpty()){
                    current = stack1.pop();
                    arr.add(current.val);
                    if(current.left != null){
                        stack2.push(current.left);
                    }
                    if(current.right != null){
                        stack2.push(current.right);
                    }
                }
                lis.add(arr);
            }
            
            if(!stack2.isEmpty()){
                arr = new ArrayList<>();
                while(!stack2.isEmpty()){
                    current = stack2.pop();
                    arr.add(current.val);
                    if(current.right != null){
                        stack1.push(current.right);
                    }
                    if(current.left != null){
                        stack1.push(current.left);
                    }
                }
                lis.add(arr);
            }
        }
        return lis;

    }
}
