class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
        int m = matrix.size();
        int n = matrix[0].size();

        vector<int> row(m), col(n);

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (!matrix[i][j]) {col[j] = 1; row[i] = 1;}
            }
        }

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (row[i] || col[j]) matrix[i][j] = 0;
            }
        }
    }
};