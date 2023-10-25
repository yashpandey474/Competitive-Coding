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

/* Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.*/
class Solution {
    static List<String> ans = new ArrayList<>();
    public static void dfs(TreeNode root, String str){
        if(root == null){
            return;
        }

        str += root.val;
        if(root.left == null && root.right == null){
            //LEAF NODE
            ans.add(str);
        }

        str += "->";
        dfs(root.left, str);
        dfs(root.right, str);
        
    }
    public List<String> binaryTreePaths(TreeNode root) {
        ans = new ArrayList<>();
        String str = "";
        dfs(root, str);

        return ans;
    }
}
