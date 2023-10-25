/*
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

int guessNumber(int n){
	long long int st = 1;
    long long int en = n;
    long long int mid;

    while(st<=en){
        mid = (st+en)/2;
        if(guess(mid) == 0){
            return mid;
        }
        if(guess(mid) < 0 ) {
            en = mid-1;
        }
        if(guess(mid) > 0 ){
            st = mid+1;
        }
    }
    return mid;
}
