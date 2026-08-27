class Solution:
    def heightChecker(self, heights):
        expected = heights[:]
        n = len(expected)
        
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if expected[j] < expected[min_index]:
                    min_index = j
            expected[i], expected[min_index] = expected[min_index], expected[i]
        
        count = 0
        for i in range(n):
            if heights[i] != expected[i]:
                count += 1
                
        return count