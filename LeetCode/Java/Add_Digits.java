/* Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
*/

class Solution {
    public int addDigits(int num) {
        int current = num; int second = num;

        while(current%10 != current){
            second = current;
            current = 0;
            while(second != 0){
                current += second%10;
                second = second/10;
            }
        }

        return current;
    }

}
