/*
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
*/

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList<Integer> arr = new ArrayList<>();

        for(int i = 0; i<nums.length; i++){
            int current = Math.abs(nums[i]);
            if(nums[current-1]>0){
                nums[current-1] = -nums[current-1];
            }
        }

        for(int i = 0; i<nums.length; i++){
            if(nums[i]>0){
                arr.add(i+1);
            }
        }

        return arr;
        

    }
}
