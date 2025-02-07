class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        unordered_map<int, int> ball_colors;
        unordered_map<int, int> color_count; 
        vector<int> result; 

        for (const auto& query : queries) {
            int x = query[0];
            int y = query[1];
            if (ball_colors.find(x) != ball_colors.end()) {
                int old_color = ball_colors[x];
                color_count[old_color]--;
                if (color_count[old_color] == 0) {
                    color_count.erase(old_color);
                }
            }
            ball_colors[x] = y;
            color_count[y]++;
            result.push_back(color_count.size());
        }

        return result;
    }
};