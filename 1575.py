# 1575. Count All Possible Routes

class Solution(object):
    count = 0
    memo = {}
    def countRoutes(self, locations, start, finish, fuel):
        self.count = 0
        self.memo = {}
        def pathFind(current, remain):
            myCase = 0
            if (current, remain) in self.memo: return self.memo[(current, remain)]
            if current == finish and fuel >= 0:
                myCase += 1
            for i in range(len(locations)):
                if i != current:
                    nextFuel = remain - abs(locations[i]-locations[current])
                    if nextFuel >= 0: myCase += pathFind(i, nextFuel)
            if (current, remain) not in self.memo: self.memo[(current, remain)] = myCase
            return myCase
        return pathFind(start, fuel) % (10**9 + 7)

sol = Solution()
print(sol.countRoutes(locations = [1,2,3], start = 0, finish = 2, fuel = 40))

#print(sol.countRoutes(locations = [4,3,1], start = 1, finish = 0, fuel = 6))
print(sol.countRoutes(locations = [4,3,1], start = 1, finish = 0, fuel = 6))

