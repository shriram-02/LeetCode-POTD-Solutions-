func uniqueXorTriplets(nums []int) int {
	var f [1 << 11]uint32
	var maxv int
	for _, v := range nums {
		maxv |= v
		f[v] = 1
	}
	shift := bits.Len32(uint32(maxv))
	n := 1 << shift
	fwht := func() { // fast walsh-hadamard transform
		// O(nlogn) convolution
		for k := 1; k*2 <= n; k *= 2 {
			for i := 0; i < n; i += k * 2 {
				for j := range k {
					u, v := f[i+j], f[i+j+k]
					f[i+j], f[i+j+k] = u+v, u-v
				}
			}
		}
	}
	fwht() // transform
	for i := range n {
		// f[i]^3 to find triplets
		// if the question asked for quadruplets, just f[i]^4
		f[i] *= f[i] * f[i]
	}
	fwht() // inverse transform
	var count uint32
	for i := range n {
		// same as: if f[i] >= n { count++ }
		count += min(1, f[i]>>shift)
	}
	return int(count)
}