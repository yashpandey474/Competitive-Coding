/*Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
*/

class Solution {
    public int partitionString(String s) {
        s = s.toLowerCase();
        HashSet<Character> set = new HashSet<>();
        int numSubstrings = 1;

        for(int i = 0; i<s.length(); i++){
            if(set.contains(s.charAt(i))){
                set.clear();
                numSubstrings++;
            }
            set.add(s.charAt(i));
        }
        return numSubstrings;
    }
}
