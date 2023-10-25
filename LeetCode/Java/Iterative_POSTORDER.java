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
    public List<Integer> postorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();

        if(root == null){
            return result;
        }

        Stack<TreeNode> stack1 = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();
        TreeNode current = root;

        stack1.push(root);

        while(!stack1.isEmpty()){
            current = stack1.pop();

            if(current == null){
                continue;
            }

            stack2.push(current);

            stack1.push(current.left);
            stack1.push(current.right);
        }

        while(!stack2.isEmpty()){
            result.add(stack2.pop().val);
        }

        return result;
    }
}
