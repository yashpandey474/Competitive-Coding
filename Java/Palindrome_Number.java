class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        Stack<Integer> stack = new Stack<>();
        int current = x; int val = 0;
        
        while(current != 0){
            val = current%10;
            current = current/10;
            stack.push(val);
        }

        current = x;
        while(current != 0){
            val = stack.pop();
            if(val != current%10){
                return false;
            }
            current = current/10;
        }

        return true;
    }
}
