class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x: (x[0], -x[1]))

        max_defense = 0
        count = 0

        for i in range(len(properties) - 1, -1, -1):

            if properties[i][1] < max_defense:
                count += 1

            max_defense = max(max_defense, properties[i][1])

        return count
        