class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Convert all strings to code# -> 
        #Have dictionary where if code# matches, append to to dictionary 

        dict1 = {}
        for x in strs:
            sort = sorted(x)
            sortString = str(sort)
            if sortString not in dict1:
                dict1[sortString] = [x]
            else:
                dict1[sortString].append(x)
            
        return list(dict1.values())