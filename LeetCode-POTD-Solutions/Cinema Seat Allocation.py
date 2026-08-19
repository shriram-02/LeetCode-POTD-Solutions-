
class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        // Store reserved seats for each row as a bitmask.
        // Bit 0 -> seat 1, bit 1 -> seat 2, ..., bit 9 -> seat 10.
        unordered_map<int, int> rows;

        for (auto &seat : reservedSeats) {
            int row = seat[0];
            int s = seat[1];

            rows[row] |= (1 << (s - 1));
        }

        int answer = (n - rows.size()) * 2;

        // Masks for the three possible 4-seat blocks:
        // 2,3,4,5
        int left = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4);

        // 4,5,6,7
        int middle = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6);

        // 6,7,8,9
        int right = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8);

        for (auto &[row, mask] : rows) {
            bool canLeft = (mask & left) == 0;
            bool canMiddle = (mask & middle) == 0;
            bool canRight = (mask & right) == 0;

            if (canLeft && canRight) {
                // Two non-overlapping groups.
                answer += 2;
            }
            else if (canLeft || canMiddle || canRight) {
                // At least one group can be placed.
                answer += 1;
            }
        }

        return answer;
    }
};

