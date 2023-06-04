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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> arr = new ArrayList<>();
        dfs(root, arr, 0);
        return arr;
    }

    public void dfs(TreeNode root, List<Integer> arr, int depth){
        if(root == null){
            return;
        }

        if(depth == arr.size()){
            arr.add(root.val);
        }

        dfs(root.right, arr, depth+1);
        dfs(root.left, arr, depth+1);
    }
}
