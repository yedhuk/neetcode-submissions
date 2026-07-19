class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = {}
        
        
        sorted_tuples = sorted(zip(position,speed),reverse=True)
        position, speed = zip(*sorted_tuples)
        position = list(position)
        speed = list(speed)
        print(position,speed)
        n = len(position)
        totalFleet = n
        prevbalTime = None
        for i in range(n):
            balanceTime = float(target - position[i])/speed[i]          

            if prevbalTime and balanceTime <= prevbalTime:
                fleet[prevbalTime] += 1

            else:
                fleet[balanceTime] = 1
                prevbalTime = balanceTime
                


            print(f"{i} -> {balanceTime} <= {prevbalTime}")
            # if balanceTime in fleet:
            #     fleet[balanceTime] += 1
                
            # else:
            #     fleet[balanceTime] = 1

        return len(fleet.keys())

        