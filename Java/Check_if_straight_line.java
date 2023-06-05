/*
You are given an array coordinates, coordinates[i] = [x, y],
where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
*/

class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        int noPoints = coordinates.length;
        int num = 0;
        int denom = 0;
        int oldSlope = 0;
        int curNum = 0; int curDenom = 0;
        Boolean all_same = false;

        if((coordinates[0][0]-coordinates[1][0]) != 0){
            oldSlope = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0]);

            num = coordinates[0][1]-coordinates[1][1];
            denom = coordinates[0][0]-coordinates[1][0];
        }
        else{
            if(coordinates[0][0] == coordinates[1][0]){
                all_same = true;
            }

            num = (coordinates[0][1]-coordinates[1][1]);
            denom = 0;
        }

        System.out.println(oldSlope);
        for(int i = 0; i<noPoints; i++){
            
            for(int j = i+1; j<noPoints; j++){
                
                curNum = (coordinates[i][1]-coordinates[j][1]);
                curDenom = (coordinates[i][0] - coordinates[j][0]);
                if(denom!=0){
                    if(curDenom == 0){
                        return false;
                    }
                    if(curNum/curDenom != oldSlope){
                        return false;
                    }
                }
                else{
                    if(all_same){
                        if(coordinates[i][0] != coordinates[j][0]){
                            return false;
                        }
                        else{
                            continue;
                        }
                    }
                    if(curNum != num || curDenom != denom){
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
