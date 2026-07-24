class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        print(f"sorted piles : {piles}")

        if h == len(piles):
            return piles[-1]

        else:
            l = 1
            r = piles[-1]

            
            mink = piles[-1]

            

            while l <= r:
                m = l + (r-l)//2
                k = m
                th = 0
                for p in piles:
                    d = p // k
                    rem = 1 if p % k > 0 else 0
                    th += (d + rem)

                if th > h:
                    l = m+1
                elif k < mink:
                    mink = k
                    r = m-1


        return mink
                
                




                


            # th = len(piles)
            # for p in piles:
            #     per_pile = p // k
            #     if per_pile > 1:
            #         th += per_pile - 1
            #         if th > k:
            #             break


        