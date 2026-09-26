class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        Map<String, String> map = new HashMap<>();
        
        for (List<String> k : knowledge) {
            map.put(k.get(0), k.get(1));
        }
        
        StringBuilder ans = new StringBuilder();
        
        for (int i = 0; i < s.length(); ) {
            if (s.charAt(i) == '(') {
                int j = i + 1;
                
                while (s.charAt(j) != ')') {
                    j++;
                }
                
                String key = s.substring(i + 1, j);
                ans.append(map.getOrDefault(key, "?"));
                i = j + 1;
            } else {
                ans.append(s.charAt(i));
                i++;
            }
        }
        
        return ans.toString();
    }
}