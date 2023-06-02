class Solution {
    public int romanToInt(String s) {
        int number = 0;
        int stringLength = s.length();

        HashMap <Character, Integer> map = new HashMap<>();
        map.put('V', 5);
        map.put('I', 1);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        for(int i = 0; i<stringLength; i++){
            int val = map.get(s.charAt(i));
            if(i != stringLength-1 && val < map.get(s.charAt(i+1))){
                number -= val;
            }
            else{
                number += val;
            }
        }
        
        return number;
    }
}
