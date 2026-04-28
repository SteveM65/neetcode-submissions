class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: <length> + <delimiter> + <string>
            # Example: ["neet","code"] -> "4#neet4#code"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the delimiter to know where the length ends
            while s[j] != "#":
                j += 1
            
            # Extract the length of the next string
            length = int(s[i:j])
            
            # Start of the actual string is right after '#'
            start = j + 1
            # End of the actual string is start + length
            end = start + length
            
            res.append(s[start:end])
            
            # Move pointer i to the start of the next encoded segment
            i = end
            
        return res