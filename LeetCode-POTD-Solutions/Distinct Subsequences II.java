
class Solution {
    public int distinctSubseqII(String s) {
        final long MOD = 1_000_000_007;
        long[] last = new long[26];

        long total = 0;

        for (char c : s.toCharArray()) {
            int x = c - 'a';

            long add = (total + 1) % MOD;
            total = (total + add - last[x] + MOD) % MOD;
            last[x] = add;
        }

        return (int) total;
    }
}

