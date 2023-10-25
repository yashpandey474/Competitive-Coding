class Solution {
    
    public static void reverse(int[] nums, int start, int end){
        while(start < end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++; end--;
        }
    }
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        if(len == 1){
            return;
        }
        
        k = k%len;
        //reverse the entire array
        reverse(nums, 0, len-1);
        
        //reverse first k elements
        reverse(nums, 0, k-1);
        
        //reverse last len-k elements
        reverse(nums, k, len-1);
        
    }
}
