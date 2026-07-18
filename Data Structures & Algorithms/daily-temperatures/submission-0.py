class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices = []
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures):

            while indices and t > temperatures[indices[-1]]:
                index = indices.pop()
                res[index] = i - index
            
            indices.append(i)
        

        return res
            





                    
            