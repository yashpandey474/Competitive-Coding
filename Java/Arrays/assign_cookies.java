/*
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i,
and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
*/

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int count = 0;
        Arrays.sort(s);
        Arrays.sort(g);

        int i = g.length-1; int j = s.length-1;

        while(i>=0 && j>=0){
            if(s[j]>=g[i]){
                count++; i--; j--;
                continue;
            }
            i--;        
        }

        return count;
    }
}
