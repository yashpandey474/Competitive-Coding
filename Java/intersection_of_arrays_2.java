/*
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
*/
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        

        int first = nums1.length; int second = nums2.length;
        ArrayList<Integer> arr = new ArrayList<>();
        int i = 0; int j = 0;
        
        while(i<first && j<second){
            if(nums1[i] == nums2[j]){
                arr.add(nums1[i]);
                i++; j++;
                continue;
            }
            if(nums1[i]<nums2[j]){
                i++;
                continue;
            }
            j++;
        }
        first = arr.size();
        int[] answer = new int[arr.size()];
        
        for( i = 0; i<first; i++){
            answer[i] = arr.get(i);
        }
        return answer;
    }
}
