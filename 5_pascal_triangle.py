class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        for i in range(1,numRows):
            temp = [1]
            for j in range(1, len(result)):
                temp.append(result[i-1][j]+result[i-1][j-1])
            temp.append(1)
            result.append(temp)
        return result
