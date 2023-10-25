class Solution {
    public int countNegatives(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        int count = 0;
        for(int i = 0; i<rows; i++){
            //FOR EVERY ARRAY

            for(int j = cols-1; j>=0; j--){
                if(grid[i][j] >= 0){
                    break;   
                }
                count++;
            }
        }

        return count;
    }
}
