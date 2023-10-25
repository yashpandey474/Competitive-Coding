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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> lis = new ArrayList<>();
        Queue<Pair> queue = new LinkedList<>();

        queue.add(new Pair(root, 0));
        Pair current;

        if(root == null){
            return lis;
        }

        int prev_level = 0; List<Integer> arr = new ArrayList<>();
        while(!queue.isEmpty()){
            current = queue.poll();
            
            if(current.level == prev_level){
                arr.add(current.node.val);
            }
            else{
                lis.add(arr);
                arr = new ArrayList<>();
                arr.add(current.node.val);
                prev_level = current.level;
            }

            if(current.node.left != null){
                queue.add(new Pair(current.node.left, current.level+1));
            }

            if(current.node.right != null){
                queue.add(new Pair(current.node.right, current.level+1));
            }
        }
        lis.add(arr);
        return lis;

    }
}
