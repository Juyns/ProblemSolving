# 406. Queue Reconstruction by Height

class Solution(object):
    def reconstructQueue(self, people):
        dic = {}
        heights = []
        if not people: return []
        for i in range(len(people)):
            height, order = people[i]
            if height not in dic:
                dic[height] = []
                heights.append(height)
            dic[height].append((order, i))
        
        heights.sort(reverse=True)
        result = []
        for h in heights:
            dic[h].sort()
            for person in dic[h]:
                result.insert(person[0], people[person[1]])
        return result
        
        
sol = Solution()
print(sol.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))