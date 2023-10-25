class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] answer = new int[n];

        int product = nums[n-1];

        for(int i = nums.length-2; i>=0; i--){
            suffix[i] = product;
            product *= nums[i];
        }

        product = nums[0];

        for(int i = 1; i<nums.length; i++){
            prefix[i] = product;
            product *= nums[i];
            if(i!=nums.length-1){
                answer[i] = prefix[i]*suffix[i];
            }
        }

        answer[0] = suffix[0];
        answer[nums.length-1] = prefix[nums.length-1];

        return answer;

    }
}
