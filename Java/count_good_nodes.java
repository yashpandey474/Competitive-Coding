/**
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

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
    public static int recGood(TreeNode root, int max, int noNodes){
        if(root == null){
            return noNodes;
        }
        if(root.val >= max){
            max = root.val;

            noNodes += 1;
            System.out.println(root.val+  " " +  noNodes);
        }

         noNodes += (recGood(root.left, max, 0)+ recGood(root.right, max, 0));
                    return noNodes;
    }
    public int goodNodes(TreeNode root) {
        return recGood(root, root.val, 0);
    }
}
