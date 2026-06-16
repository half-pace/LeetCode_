class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        while k > 0:
            i = max(seen, key = seen.get)
            res.append(i)
            seen.pop(i)
            k -= 1
        return sorted(res)