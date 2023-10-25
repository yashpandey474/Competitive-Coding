class Solution {
    public int[] plusOne(int[] digits) {
        int noDigits = digits.length;
        int carry = 1; int sum = 0;

        for(int i = noDigits-1; i>=0; i--){
            sum = digits[i] + carry;
            digits[i] = sum%10;
            carry = sum/10;
        }

        if(carry == 1){
            int[] ndigits = new int[noDigits + 1];

            ndigits[0] = carry;

            for(int i = 0; i<noDigits; i++){
                ndigits[i+1] = digits[i];
            }

            return ndigits;
        }

        return digits;
    }
}
