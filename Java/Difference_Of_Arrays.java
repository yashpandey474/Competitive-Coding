class RandomizedSet {
    HashSet<Integer> set = new HashSet<>();


    public RandomizedSet() {
        this.set.clear();
    }
    
    public boolean insert(int val) {
        return this.set.add(val);
    }
    
    public boolean remove(int val) {
        if(this.set.contains(val)){
            this.set.remove(val);
            return true;
        }
        return false;
    }
    
    public int getRandom() {
        ArrayList<Integer> setList = new ArrayList<>(this.set);
        int index = (int) (Math.random() * this.set.size());
        return setList.get(index);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
