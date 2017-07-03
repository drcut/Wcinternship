class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            rtype = []
        elif numRows == 1:
            rtype = [[1]]
        elif numRows == 2:
            rtype = [[1],[1,1]]
        else:
            rtype = [[1],[1,1]]
            for id in range(3,numRows+1):
                tmp = [1]
                for tid in range(1,id-1):
                    tmp.append(rtype[id-2][tid-1] + rtype[id-2][tid])
                tmp.append(1)
                rtype.append(tmp)
        return rtype