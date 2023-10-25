class Solution {
    public String reverseVowels(String s) {
        Stack<Character> st = new Stack<>();
        String s1 = s;
        String s2 = new String("");
        HashSet<Character> set = new HashSet<>();

        set.add('a'); set.add('e'); set.add('o'); set.add('i'); set.add('u');
        set.add('A'); set.add('E'); set.add('O'); set.add('I'); set.add('U');
        int stLen = s.length();

        for(int i = 0; i<stLen; i++){
            if(set.contains(s.charAt(i))){
                st.push(s.charAt(i));
            }
        }

        for(int i = 0; i<stLen; i++){
            if(set.contains(s.charAt(i))){
                s2 += st.pop() + "";
            }else{
                s2 += s.charAt(i) + "";
            }
        }

        return s2;

    }
}
