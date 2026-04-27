class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Put into key:values, key:count
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)
        
        arr = []

      #Add dictionary as list of pairs, sort by count
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        print(arr)

        #Add into answer values by highest count, and pop
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


        