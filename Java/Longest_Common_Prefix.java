/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
*/

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 1){
            return strs[0];
        }
        
        //STRING TO BE RETURNED
        String temp = "";

        //SORT THE ARRAY OF STRINGS
        Arrays.sort(strs);

        //COMPARE FIRST STRING WITH STRINGS FROM END
        for(int i = 0, j = strs.length-1; i<strs[0].length(); i++){
            
            //IF BOTH STRINGS ARE NON NULL
            if(strs[0] != "" && strs[j] != ""){
                //IOF THE CHARACTERS ARE CORRECT
                if(strs[0].charAt(i) == strs[j].charAt(i)){
                    temp += strs[0].charAt(i);
                }
                //CHARACTERS NOT EQUAL
                else{
                    break;
                }
            }
            //IF STRINGS ARE NULL
            else{
                break;
            }
        }
        return temp;
        
    }
}
