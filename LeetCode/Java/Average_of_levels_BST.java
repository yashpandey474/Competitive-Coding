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
    public List<Double> averageOfLevels(TreeNode root) {
        //INITIAL NODE AT 1ST LEVEL
        Pair p = new Pair(root, 0);
        List<Double> ret = new ArrayList<Double>();
        Queue<Pair> q = new LinkedList<>();

        //ADD THE QUEUE AND INITIALISE
        q.add(p);
        int prev_level = 0; long sum = 0; int count = 0;
        while(!q.isEmpty()){
            //REMOVE A NODE FROM THE QUEUE
            p = q.poll();

            //IF AT CURRENT LEVEL
            if(p.level == prev_level){
                sum+=p.node.val;
                count+=1;
                System.out.println("SAME LEVEL" + p.node.val + " " + sum + " " + count);
            }
            else{
                //IF AT NEXT LEVEL
                ret.add((double)sum/count);
                sum = p.node.val;
                count = 1;
                //CHANGE LEVEL
                prev_level = p.level;

                System.out.println("NEXT LEVEL" + p.node.val + " " + sum + " " + count);

            }
            if(p.node.left != null){
                q.add(new Pair(p.node.left, p.level+1));
            }
            if(p.node.right !=  null){
                q.add(new Pair(p.node.right, p.level+1));
            }
        }

        //PUSH THE FINAL ANSWER
        ret.add((double)sum/count);
        return ret;

    }
}
