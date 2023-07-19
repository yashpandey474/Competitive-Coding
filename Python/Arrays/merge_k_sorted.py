import java.util.* ;
import java.io.*; 
import java.util.ArrayList;


class Element{
	int ele;
	int arrIndex;
	int indexInArr;

	Element(int ele, int arrIndex, int indexInArr){
		this.ele = ele;
		this.arrIndex = arrIndex;
		this.indexInArr = indexInArr;
	}
}

class sortByEle implements Comparator<Element>{
	public int compare(Element a, Element b){
		return a.ele - b.ele;
	}
}
public class Solution 
{
	public static ArrayList<Integer> mergeKSortedArrays(ArrayList<ArrayList<Integer>> kArrays, int k)
	{
		// Write your code here.

		//CREATE A PRIORITY QUEUE
		PriorityQueue<Element> pq = new PriorityQueue(new sortByEle());

		//ADD K ELEMENTS TO PQ
		for (int i = 0; i<k; i++){
			pq.add(new Element(
				kArrays.get(i).get(0),
				i,
				0
			));
		}

		//ADD TO RESULT
		ArrayList<Integer> result = new ArrayList<>();

		while (!pq.isEmpty()){
			//ADD TO RESULT
			Element e = pq.poll();
			result.add(e.ele);
			//GET NEXT ELEMENT FROM THAT ARRAY IF IT HAS ANOTHER ELEMENT
			if (e.indexInArr < kArrays.get(e.arrIndex).size()-1){
				pq.add(new Element(
					kArrays.get(e.arrIndex).get(e.indexInArr + 1),
					e.arrIndex,
					e.indexInArr+1
				));
			}
		}
		return result;
	}
}
