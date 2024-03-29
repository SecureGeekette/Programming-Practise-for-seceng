14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Solution:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        common_prefix = strs[0]

        for word in strs[1:]:
            i = 0
            while i < len(word) and i < len(common_prefix) and common_prefix[i] == word[i]:
                i += 1
                
            common_prefix = common_prefix[:i]
                

        return common_prefix


Mistakes I made 
- I'm not running through all the possible test cases. I have to think through all possible scenarios and test cases

The more intuitive solution but more time consuming one was:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""

        if not strs:
            return ans

        for j in range(len(strs[0])):
            for i in range(len(strs)-1):
                if strs[i][:j+1] != strs[i+1][:j+1]:
                    return ans
            ans = "".join([ans,strs[0][j]])

        return ans
        
        
