class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def helper(s,path):
            if not s:
                ans.append(path[:])
                return
            for i in range(0,len(s)):
                temp=s[:i+1]
                if temp==temp[::-1]:
                    path.append(s[:i+1])
                    helper(s[i+1:],path)
                    path.pop()
        helper(s,[])
        return ans
