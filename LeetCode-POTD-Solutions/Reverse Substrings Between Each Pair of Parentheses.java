class Solution {
    public String reverseParentheses(String s) {
        java.util.Stack<StringBuilder> stack = new java.util.Stack<>();
        StringBuilder curr = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(curr);
                curr = new StringBuilder();
            } else if (c == ')') {
                curr.reverse();
                curr = stack.pop().append(curr);
            } else {
                curr.append(c);
            }
        }

        return curr.toString();
    }
}