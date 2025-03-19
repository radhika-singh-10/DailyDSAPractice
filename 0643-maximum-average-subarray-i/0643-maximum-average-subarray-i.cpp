#include <limits>
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        int sum=0.0;

        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        int res = sum;
        for(int i=k;i<nums.size();i++){
            sum+=nums[i]-nums[i-k];
            res=max(res,sum);
        }
        return (double)res/k;
    }
};