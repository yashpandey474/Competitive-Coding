import java.util.*;

class Element{
    int ele;
    int freq;

    Element(int ele, int freq){
        this.ele = ele;
        this.freq = freq;
    }
}

class sortByFreq implements Comparator<Element>{
    public int compare(Element a, Element b){
        return a.freq - b.freq;
    }
}
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        PriorityQueue<Element> pq = new PriorityQueue<>(new sortByFreq());
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry: map.entrySet()){
            if (pq.size() < k){
                pq.add(new Element(entry.getKey(), entry.getValue()));
            }
            else{
                if (pq.peek().freq < entry.getValue()){
                    pq.poll();
                    pq.add(new Element(entry.getKey(), entry.getValue()));
                }
            }
        }
        int[] arr = new int[pq.size()];
        int i = 0;
        Iterator<Element> it = pq.iterator();
        while (it.hasNext()){
            int element = it.next().ele;
            arr[i] = element;

            i+=1;
        }

        return arr;
        
    }
}
