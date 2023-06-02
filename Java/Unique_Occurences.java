/*Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
*/


class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        //IF NUMBER OF OCCURENCES OF EACH VALUE IS UNIQUE

        //STORES THE NUMBER OF OCCURENCES OF EACH VALUE
        HashMap<Integer, Integer> occurences = new HashMap<>();
        int length = arr.length;

        for(int i = 0; i<length; i++){
            if(occurences.containsKey(arr[i])){
                occurences.put(arr[i],occurences.get(arr[i])+1);
            }
            else{
                occurences.put(arr[i],1);
            }
        }

        HashSet<Integer> set = new HashSet<>();

        for (Map.Entry<Integer,Integer> mapElement : occurences.entrySet()) {
            if(set.contains(mapElement.getValue())){
                return false;
            }
            set.add(mapElement.getValue());
        }
        return true;
    }
}
