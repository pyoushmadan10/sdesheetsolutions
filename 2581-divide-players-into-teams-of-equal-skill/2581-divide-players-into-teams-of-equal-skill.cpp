class Solution {
public:
        long long dividePlayers(vector<int>& skill) {
        int players[1001] = {0}, weak = INT_MAX, strong = 0;
        for (int player : skill) {
            players[player]++;
            weak = min(weak, player);
            strong = max(strong, player);
        }

        long long chemistry = 0;
        for (; weak <= strong; weak++, strong--) {
            // Check if count of weak and strong players are same
            if (players[weak] != players[strong])
                return -1;
            if (players[weak])
                chemistry += weak * strong * long(weak == strong ? players[weak] / 2 :  players[weak]);
        }

        return chemistry;
    }
};