class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b = 0, len(matrix)-1
        l,r = 0, len(matrix[0]) - 1
        print(f"Top - {t}, Bottom - {b}")
        while t <= b:
            m = t + (b-t)//2

            if matrix[m][0] < target and matrix[m][-1] < target:
                t = m+1
            elif matrix[m][0] > target and matrix[m][-1] > target:
                b = m-1
            else:
                while l <=r:
                    m2 = l + (r-l)//2

                    if matrix[m][m2] < target:
                        l = m2 + 1

                    elif matrix[m][m2] > target:
                        r = m2 - 1

                    else:
                        return True
                return False
            
        return False


        