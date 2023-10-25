class Solution {
    public int lengthOfLastWord(String s) {
        //RETURN THE LENGTH OF LAST SUBSTRING WITH NO SPACES

        int length = 0;
        int i;

        //FIND POSITION OF LAST CHARACTER
        for(i = s.length()-1; i>=0; i--){
            if(s.charAt(i)!= ' '){
                break;
            }
        }

        //FIND LENGTH OF WORD
        for(; i>=0; i--){
            if(s.charAt(i) == ' '){
                break;
            }
            length++;
        }

        return length;

    }
}
