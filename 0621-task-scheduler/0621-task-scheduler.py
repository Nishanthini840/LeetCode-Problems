class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26

        for task in tasks:
            index = ord(task) - ord('A')
            count[index] += 1

        max_freq = max(count)

        max_count = 0

        for x in count:
            if x == max_freq:
                max_count += 1

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_count
        )
        