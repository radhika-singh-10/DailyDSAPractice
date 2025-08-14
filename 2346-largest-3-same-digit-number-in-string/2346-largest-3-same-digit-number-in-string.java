class Solution {
    public String largestGoodInteger(String num) {
        int n=num.length();
        char maxDigit='\0';
        for(int i=0;i<=n-3;i++){
            if(num.charAt(i)==num.charAt(i+1)&& num.charAt(i+1)==num.charAt(i+2)){
                maxDigit=(char)Math.max(maxDigit,num.charAt(i));
            }
        }
        return maxDigit=='\0'?"":new String(new char[]{maxDigit, maxDigit, maxDigit});


        // int len=num.length;
        // HashMap<String,Integer> counter=new Map();
        // boolean check=False;
        // int l=0;
        // int n=0;
        // for(int r=0;r<len;r++){
        //     int temp=0;
        //     while(r<len-1 && l-r+1<3 && num[r]==num[l]){
        //         temp=String.toInteger(num[r]);
        //         r+=1;
        //     }
        //     n=max(temp,n);
        // }
        // return n.toString();
    }
}