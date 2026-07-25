class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        print(key,value,timestamp)
        if key not in self.timemap:
            self.timemap[key] = []
            
        self.timemap[key].append([timestamp, value])
        print(self.timemap)


        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        ts = self.timemap.get(key,None)
        print(ts)
        n = len(ts)-1 if ts else 0
        if ts:
           l = 0
           r = len(ts)-1
           
           while l <= r:

                m = l + (r-l)//2
                print(f"m->{m} ; ts[m][0]->{ts[m][0]}")
                if ts[m][0] <= timestamp:
                    res = ts[m][1]
                    l = m+1
                else:
                    r = m-1
        #    if 0 <= l < n and 0 <= r <= n:

        #     if (timestamp - ts[l][0]) > (timestamp - ts[r][0]):
        #         return ts[r][1]
        #     else:
        #         return ts[l][1]
        #    elif 0 <= r <= n:
        #      return ts[r][1]
        #    else:
        #      return ts[l][1]


            
        return res
            
        
