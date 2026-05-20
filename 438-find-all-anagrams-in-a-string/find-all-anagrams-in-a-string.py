class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sorted_p = sorted(p)
        key  = ""
        group = []
        
        if len(p) > len(s):
            return group

        key = s[:len(p)]
        sorted_key = sorted(key)
        if sorted_key == sorted_p:
            group.append(0)

        for i in range(len(p), len(s)):
            key += s[i]
            key = key[1:]
            sorted_key= sorted(key)
            if sorted_key == sorted_p:
                group.append(i- len(p) +1)

        return group

        
        


        


            
