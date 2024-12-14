#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        // Map to store the frequency of elements in the current window
        map<int, int> freqMap;
        
        // Two pointers for the sliding window
        int i = 0, j = 0;
        int n = nums.size();
        
        // Variable to store the total count of valid subarrays
        long long ans = 0;

        // Iterate through the array using the 'j' pointer
        while (j < n) {
            // Step 1: Include the current element into the window
            freqMap[nums[j]]++;

            // Step 2: Ensure the current window is valid
            // A window is valid if the difference between the maximum and minimum element is ≤ 2
            while (freqMap.rbegin()->first - freqMap.begin()->first > 2) {
                // Decrement the frequency of the element at 'i'
                freqMap[nums[i]]--;
                // Remove the element from the map if its frequency becomes 0
                if (freqMap[nums[i]] == 0) {
                    freqMap.erase(nums[i]);
                }
                // Shrink the window by moving the 'i' pointer
                i++;
            }

            // Step 3: Count all valid subarrays ending at index 'j'
            ans += j - i + 1;

            // Expand the window by moving the 'j' pointer
            j++;
        }

        // Return the total count of valid subarrays
        return ans;
    }
};