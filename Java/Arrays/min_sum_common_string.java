class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String, Integer> map1 = new HashMap<>();
        ArrayList<String> arr = new ArrayList<>();
        int minSum = -1;

        for(int i = 0; i<list1.length; i++){
            map1.put(list1[i], i);
        }
        
        for(int j = 0; j<list2.length; j++){
            if(map1.containsKey(list2[j])){
                if(minSum == -1 || minSum > j + map1.get(list2[j])){
                    minSum = j + map1.get(list2[j]);
                    arr = new ArrayList<>();
                    arr.add(list2[j]);
                }

                else if (minSum == j + map1.get(list2[j])){
                    arr.add(list2[j]);
                }
            }
        }
        int len = arr.size();
        String[] ans = new String[len];
        for(int i = 0; i<len; i++){
            ans[i] = arr.get(i);
        }

        return ans;
    }
}
