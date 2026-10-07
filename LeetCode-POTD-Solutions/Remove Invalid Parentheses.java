	class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> ans = new ArrayList<>();
        
        int left = 0, right = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                left++;
            } else if (c == ')') {
                if (left > 0) {
                    left--;
                } else {
                    right++;
                }
            }
        }

        dfs(s, 0, left, right, ans);

        return ans;
    }

    private void dfs(String s, int start, int left, int right, List<String> ans) {
        if (left == 0 && right == 0) {
            if (isValid(s)) {
                ans.add(s);
            }
            return;
        }

        for (int i = start; i < s.length(); i++) {
            if (i > start && s.charAt(i) == s.charAt(i - 1)) {
                continue;
            }

            if (left + right > s.length() - i) {
                break;
            }

            char c = s.charAt(i);

            if (left > 0 && c == '(') {
                dfs(
                    s.substring(0, i) + s.substring(i + 1),
                    i,
                    left - 1,
                    right,
                    ans
                );
            }

            if (right > 0 && c == ')') {
                dfs(
                    s.substring(0, i) + s.substring(i + 1),
                    i,
                    left,
                    right - 1,
                    ans
                );
            }
        }
    }

    private boolean isValid(String s) {
        int balance = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                balance++;
            } else if (c == ')') {
                balance--;

                if (balance < 0) {
                    return false;
                }
            }
        }

        return balance == 0;
    }
}