class Solution(object):
    def pancakeSort(self, arr):
        result = []
        n = len(arr)

        for size in range(n, 1, -1):
            index = arr.index(size)

            if index != 0:
                arr[:index + 1] = arr[:index + 1][::-1]
                result.append(index + 1)

            arr[:size] = arr[:size][::-1]
            result.append(size)

        return result