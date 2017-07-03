class Solution(object):
    def getRow(self, rowIndex):
        rowIndex = rowIndex+1
        if rowIndex == 0:
            rtype = []
        elif rowIndex == 1:
            rtype = [1]
        elif rowIndex == 2:
            rtype = [1,1]
        else:
            rtype = [1,1]
            for id in range(3,rowIndex + 1):
                tmp = [1]
                for tid in range(1,id - 1):
                    tmp.append(rtype[tid - 1] + rtype[tid])
                tmp.append(1)
                rtype = tmp
        return rtype