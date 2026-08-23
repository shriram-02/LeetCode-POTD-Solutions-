class Solution {
public:
    bool sumGame(string num) {
        int n = num.size(), half = n / 2;
        int leftQ = 0, rightQ = 0;
        int diff = 0;

        for (int i = 0; i < half; i++) {
            if (num[i] == '?')
                leftQ++;
            else
                diff += num[i] - '0';
        }

        for (int i = half; i < n; i++) {
            if (num[i] == '?')
                rightQ++;
            else
                diff -= num[i] - '0';
        }

        if ((leftQ + rightQ) % 2)
            return true;

        int qDiff = leftQ - rightQ;

        // Bob can force equality iff:
        // diff + 9 * (qDiff / 2) == 0
        return diff + 9 * (qDiff / 2) != 0;
    }
};