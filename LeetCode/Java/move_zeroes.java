class Solution {
    public void moveZeroes(int[] nums) {
        //O(N) SPACE
        int len = nums.length;
        int count = 0;
        
        for(int i = 0; i<len; i++){
            if(nums[i] != 0){
                int temp = nums[count];
                nums[count] = nums[i];
                nums[i] = temp;
                count += 1;
            }
        }
        
        
    }
}
