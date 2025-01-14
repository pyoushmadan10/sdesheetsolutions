class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        const int n = A.size();
        vector<int> ans(n, 0);
        bitset<101> seen = {0}; // Tracks presence of elements (up to 2*n indices)
        int count = 0;

        for (int i = 0; i < n; i++) {
            int a = A[i], b = B[i];
            
            // Mark A[i] in bitset
            seen[2 * a - 1] = 1;
            if (seen[2 * a] == 1) count++; // If B already marked it
            
            // Mark B[i] in bitset
            seen[2 * b] = 1;
            if (seen[2 * b - 1] == 1) count++; // If A already marked it

            // Update result array
            ans[i] = count;
        }

        return ans;
    }
};