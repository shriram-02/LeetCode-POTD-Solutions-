class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> prefixes;

        // Store all prefixes from arr1
        for (int x : arr1) {
            while (x > 0) {
                prefixes.insert(x);
                x /= 10;
            }
        }

        int ans = 0;

        // Check prefixes from arr2
        for (int y : arr2) {
            int temp = y;

            while (temp > 0) {
                if (prefixes.count(temp)) {
                    ans = max(ans, (int)to_string(temp).size());
                    break; // longest prefix for this number found
                }
                temp /= 10;
            }
        }

        return ans;
    }
};