class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = set()
        pos_diags = set()  # (row + col)
        neg_diags = set()  # (row - col)
        
        def backtrack(row):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
                    continue
                
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                
                count += backtrack(row + 1)
        
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)
                
            return count
            
        return backtrack(0)
       
        