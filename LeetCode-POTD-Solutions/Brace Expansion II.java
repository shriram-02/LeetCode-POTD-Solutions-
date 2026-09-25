class Solution {
    public List<String> braceExpansionII(String expression) {
        Set<String> result = parse(expression, new int[]{0});
        List<String> ans = new ArrayList<>(result);
        Collections.sort(ans);
        return ans;
    }

    private Set<String> parse(String s, int[] idx) {
        Set<String> result = new HashSet<>();
        Set<String> current = new HashSet<>();
        current.add("");

        while (idx[0] < s.length() && s.charAt(idx[0]) != '}') {
            char ch = s.charAt(idx[0]);

            if (ch == ',') {
                result.addAll(current);
                current = new HashSet<>();
                current.add("");
                idx[0]++;
            } else {
                Set<String> next;

                if (ch == '{') {
                    idx[0]++;
                    next = parse(s, idx);
                    idx[0]++;
                } else {
                    next = new HashSet<>();
                    next.add(String.valueOf(ch));
                    idx[0]++;
                }

                Set<String> combined = new HashSet<>();

                for (String a : current) {
                    for (String b : next) {
                        combined.add(a + b);
                    }
                }

                current = combined;
            }
        }

        result.addAll(current);
        return result;
    }
}