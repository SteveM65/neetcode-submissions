class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Notes: 
        # Use dic[] = [value], and then .append(x)
        # Convert dictionary to list using list()

        # Steps:
        # Iterate through list
        # Sort each word 
        # Add word to dictionary based on sorted word 
        
        dict1 = {}
        for x in strs:
            sort = sorted(x)
            sortString = str(sort)
            if sortString not in dict1:
                dict1[sortString] = [x]
            else:
                dict1[sortString].append(x)
            
        return list(dict1.values())