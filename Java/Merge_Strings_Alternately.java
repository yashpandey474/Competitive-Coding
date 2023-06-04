class Solution {
    public String mergeAlternately(String word1, String word2) {
        int smaller = word2.length();
        if(word1.length() < word2.length()){
            smaller = word1.length();
        }   

        String ans = new String(); int i = 0;
        for(i = 0; i<smaller; i++){
            ans += word1.charAt(i);
            ans += word2.charAt(i);
        }

        if(smaller == word2.length()){
            for(; i<word1.length(); i++){
                ans += word1.charAt(i);
            }
        }
        else{
            for(; i<word2.length(); i++){
                ans += word2.charAt(i);
            }
        }

        return ans;
    }
}
