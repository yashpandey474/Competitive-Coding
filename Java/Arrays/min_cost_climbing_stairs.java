class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] mincost = new int[cost.length];
        mincost[0] = 0;
        mincost[1] = 0;

        if(cost.length == 2){
            return Math.min(cost[0], cost[1]);
        }
        //MINCOST[i] = min cost to reach ith step
        for(int i = 2; i<cost.length; i++){
            mincost[i] = Math.min(cost[i-1]+mincost[i-1],
            cost[i-2]+mincost[i-2]);
        }

        return Math.min(mincost[cost.length-1]+cost[cost.length-1], mincost[cost.length-2]+cost[cost.length-2]);
    }
}
