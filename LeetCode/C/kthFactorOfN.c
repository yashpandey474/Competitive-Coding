int kthFactor(int n, int k){
    for(int i = 1; i<=n; i++){
        if(n%i == 0){
            k--;
            if(!k){
                return i;
            }
        }
    }
    return -1;
}
