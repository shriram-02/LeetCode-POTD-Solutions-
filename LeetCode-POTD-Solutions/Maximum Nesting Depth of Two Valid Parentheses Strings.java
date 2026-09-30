class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int[] answer = new int[seq.length()];
        int depth = 0;

        for (int i = 0; i < seq.length(); i++) {
            if (seq.charAt(i) == '(') {
                depth++;
                answer[i] = depth % 2;
            } else {
                answer[i] = depth % 2;
                depth--;
            }
        }

        return answer;
    }
}