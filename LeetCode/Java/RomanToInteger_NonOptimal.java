class Solution {
    public int romanToInt(String s) {
        int number = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == 'X'){
                number += 10;
                if(i!=0 && s.charAt(i-1) == 'I'){
                    number -=2;
                }
                                System.out.println(s.charAt(i) + " " + number);
            }
            else if (s.charAt(i) == 'V'){
                number += 5;
                if(i!=0 && s.charAt(i-1) == 'I'){
                    number-=2;
                }
                                System.out.println(s.charAt(i) + " " + number);
            }
            else if (s.charAt(i) == 'I'){
                number+=1;
                                System.out.println(s.charAt(i) + " " + number);
            }
            else if (s.charAt(i) == 'L'){
                number += 50;
                if(i!=0 && s.charAt(i-1) == 'X'){
                    number -= 20;
                }
                                System.out.println(s.charAt(i) + " " + number);
            }
            else if (s.charAt(i) == 'C'){
                number += 100;
                if(i!=0 && s.charAt(i-1) == 'X'){
                    number -= 20;
                }

                System.out.println(s.charAt(i) + " " + number);
            }
            else if (s.charAt(i) == 'D'){
                number += 500;
                if(i!=0 && s.charAt(i-1) == 'C'){
                    number -= 200;
                }
                                System.out.println(s.charAt(i) + " " + number);
            }
            
            else if(s.charAt(i) == 'M'){
                number += 1000;
                if(i!=0 && s.charAt(i-1) == 'C'){
                    number -= 200;
                }
                                System.out.println(s.charAt(i) + " " + number);
            }
        }
        return number;
    }
}
