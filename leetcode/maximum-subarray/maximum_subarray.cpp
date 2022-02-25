#include <iostream>
#include <vector>
#include <limits.h>

class Solution {
public:
    int maxSubArray(std::vector<int>& nums, int n) {
        int MAX = INT_MIN;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            MAX = std::max(sum, MAX);
            if (sum < 0) {
                sum = 0;
            }
        }
        return MAX;
    }    
};

int main() {
    return 0;
}
