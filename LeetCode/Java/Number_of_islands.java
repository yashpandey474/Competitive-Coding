class Solution {

    public void makeTwo(char[][] grid, int row, int column){
        int totalRows = grid.length; int totalCols = grid[0].length;

        if(row < 0 || column<0 || row>=totalRows || column>=totalCols){
            return;
        } 
        if(grid[row][column] == '0'){
            return;
        }
        if(grid[row][column] == '2'){
            return;
        }
        if(grid[row][column] == '1'){
            grid[row][column] = '2';
            makeTwo(grid, row, column+1);
            makeTwo(grid, row, column-1);
            makeTwo(grid, row-1, column);
            makeTwo(grid, row+1,column);

        }
    }
    public int numIslands(char[][] grid) {
        int noIslands = 0;
        for(int i = 0; i<grid.length; i++){
            for(int j = 0; j<grid[0].length; j++){
                if(grid[i][j] == '0' || grid[i][j] == '2'){

                }
                else{
                    noIslands+=1;
                    makeTwo(grid, i, j+1);
                    makeTwo(grid, i, j-1);
                    makeTwo(grid, i-1, j);
                    makeTwo(grid, i+1, j);
                }
            }
        }

        return noIslands;
    }
}
