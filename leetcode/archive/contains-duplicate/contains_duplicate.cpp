#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
    public:
        bool containsDuplicate(std::vector<int> &nums) {
            std::unordered_set<int> set;
            for (int n : nums) {
                if (!set.insert(n).second) {
                    return true;
                }
            }
            return false;
    }
};

int main() {
    return 0;
}

