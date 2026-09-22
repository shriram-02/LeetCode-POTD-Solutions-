class Solution {
    int n, k;
    Node[] tree;

    class Node {
        int prod;
        int[] cnt;

        Node() {
            prod = 1;
            cnt = new int[k];
        }
    }

    Node merge(Node a, Node b) {
        Node res = new Node();

        res.prod = (a.prod * b.prod) % k;

        for (int r = 0; r < k; r++) {
            res.cnt[r] += a.cnt[r];
            res.cnt[(r * a.prod) % k] += b.cnt[r];
        }

        return res;
    }

    void build(int idx, int l, int r, int[] nums) {
        if (l == r) {
            tree[idx] = new Node();
            tree[idx].prod = nums[l] % k;
            tree[idx].cnt[nums[l] % k] = 1;
            return;
        }

        int mid = (l + r) / 2;

        build(idx * 2, l, mid, nums);
        build(idx * 2 + 1, mid + 1, r, nums);

        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    void update(int idx, int l, int r, int pos, int val) {
        if (l == r) {
            tree[idx] = new Node();
            tree[idx].prod = val % k;
            tree[idx].cnt[val % k] = 1;
            return;
        }

        int mid = (l + r) / 2;

        if (pos <= mid) {
            update(idx * 2, l, mid, pos, val);
        } else {
            update(idx * 2 + 1, mid + 1, r, pos, val);
        }

        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    Node query(int idx, int l, int r, int ql) {
        if (l >= ql) {
            return tree[idx];
        }

        int mid = (l + r) / 2;

        if (ql > mid) {
            return query(idx * 2 + 1, mid + 1, r, ql);
        }

        Node left = query(idx * 2, l, mid, ql);
        Node right = query(idx * 2 + 1, mid + 1, r, ql);

        return merge(left, right);
    }

    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.n = nums.length;
        this.k = k;

        tree = new Node[4 * n];

        build(1, 0, n - 1, nums);

        int[] ans = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int index = queries[i][0];
            int value = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];

            update(1, 0, n - 1, index, value);

            Node res = query(1, 0, n - 1, start);

            ans[i] = res.cnt[x];
        }

        return ans;
    }
}