lass Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> prq = new PriorityQueue<>();
        int current_size = 0;
        for(int i = 0; i<nums.length;i++){
            if (current_size == k){
                if (nums[i] > prq.peek()){
                    prq.poll();
                    prq.add(nums[i]);
                }
            }
            else{
                prq.add(nums[i]);
                current_size += 1;
            }
        }  

        return prq.poll();

        
    }
}
