class Solution {
    public int snakesAndLadders(int[][] board) {
        //CONVERT INTO 1D ARRAY
        //NEIGHBOURS: NEXT 6 ELEMENTS IN ARRAY
        int totalRows = board.length; //NUMBER OF ROWS
        int totalColumns = board[0].length;

        ArrayList<Integer> arr = new ArrayList<>();
        boolean leftRight = true;
        //Form the flat board [1D ARRAY]
        for(int i = totalRows-1; i>= 0; i--){

            if(leftRight){
                for(int j = 0; j<totalColumns; j++){
                    arr.add(board[i][j]);
                }
            }
            else{
                for(int j = totalColumns-1; j>=0 ; j--){
                    arr.add(board[i][j]);
                }
            }

            leftRight = !leftRight;
        }


        //BREADTH FIRST SEARCH
        
        //ARRAY STORING MINIMUM MOVES FOR AN ELEMENT
        int[] minMoves = new int[totalRows*totalColumns];
        for(int i = 0; i<totalRows*totalColumns; i++){
            minMoves[i] = -1;
        }

        //BFS
        Queue<Integer> queue = new LinkedList<>();
        //STARTING ELEMENT
        queue.add(0);
        minMoves[0] = 0;
        int current = 0;
        int next = 0;

        while(!queue.isEmpty()){
            current = queue.poll();

            //GOAL CHECK
            if(current == totalRows*totalRows-1){
                return minMoves[current];
            }

            //EXPLORE NEIGHBOURS
            for(int i = 1; i<= 6; i++){
                next = current + i;

                if(next > totalRows*totalRows - 1){
                    break;
                }

                //HAS SNAKE OR LADDER
                if(arr.get(next) != -1){
                    next = arr.get(next) -1;;
                }

                //NO SNAKE OR LADDER: NOT EXPLORED
                if(minMoves[next] == -1){
                    minMoves[next] = minMoves[current] + 1;
                    queue.add(next);
                }

            }


            
        }

        //NO WAY TO REACH
        return -1;




    }
}
