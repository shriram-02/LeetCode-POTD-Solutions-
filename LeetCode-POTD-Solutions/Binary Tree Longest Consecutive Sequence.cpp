class Solution(object):
    def longestConsecutive(self, root):
        if not root:
            return 0

        ans = 1

        def dfs(node, length):
            nonlocal ans

            if not node:
                return

            ans = max(ans, length)

            if node.left:
                if node.left.val == node.val + 1:
                    dfs(node.left, length + 1)
                else:
                    dfs(node.left, 1)

            if node.right:
                if node.right.val == node.val + 1:
                    dfs(node.right, length + 1)
                else:
                    dfs(node.right, 1)

        dfs(root, 1)
        return ans