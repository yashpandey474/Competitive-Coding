bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    if(n == 0){
        return true;//ALWAYS TRUE
    }

    for(int i = 0; i<flowerbedSize && n>0; i++){
        if(flowerbed[i] == 0 && (i==0 || flowerbed[i-1] == 0) && (i==flowerbedSize-1 || flowerbed[i+1] == 0)){
            flowerbed[i] = 1;
            n--;
            
        }
    }
    return n==0;
}
