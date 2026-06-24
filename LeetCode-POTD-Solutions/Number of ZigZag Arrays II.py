class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        K = r - l + 1
        
        # Total number of states is 2 * K
        # State index mapping:
        # (v, 0) -> v
        # (v, 1) -> K + v
        SIZE = 2 * K
        
        # Build the transition matrix T
        # T[i][j] represents the number of ways to transition from state j to state i
        T = [[0] * SIZE for _ in range(SIZE)]
        
        for prev in range(K):
            # From state (prev, 0) -> next value v must be < prev, new state (v, 1)
            for v in range(prev):
                T[K + v][prev] = 1
                
            # From state (prev, 1) -> next value v must be > prev, new state (v, 0)
            for v in range(prev + 1, K):
                T[v][K + prev] = 1
                
        # Helper function for matrix multiplication
        def multiply(A, B):
            C = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                for k in range(SIZE):
                    if A[i][k] == 0:
                        continue
                    for j in range(SIZE):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        # Helper function for matrix exponentiation
        def power(matrix, p):
            res = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                res[i][i] = 1
            base = matrix
            while p > 0:
                if p & 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p >>= 1
            return res

        # Base case for n = 2:
        # Valid pairs are any two distinct elements.
        # If v > prev, it counts towards direction 0. If v < prev, direction 1.
        # Initial vector representation of counts after length 2
        V = [0] * SIZE
        for prev in range(K):
            for v in range(K):
                if v > prev:
                    V[v] += 1       # state (v, 0)
                elif v < prev:
                    V[K + v] += 1   # state (v, 1)
                    
        # If n = 2, we just sum up the initial valid transitions
        if n == 2:
            return sum(V) % MOD

        # Exponentiate the matrix to transition from length 2 to length n
        T_pow = power(T, n - 2)
        
        # Multiply T_pow by the initial vector V
        ans = 0
        for i in range(SIZE):
            total_for_state_i = 0
            for j in range(SIZE):
                total_for_state_i = (total_for_state_i + T_pow[i][j] * V[j]) % MOD
            ans = (ans + total_for_state_i) % MOD
            
        return ans