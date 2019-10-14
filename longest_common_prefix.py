# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z.

class solution:
    def prefix(self,strs:[str]) -> str:
        strslen=[len(strs[a]) for a in range(len(strs))]
        k=min(strslen)
        minindex=[p for p,t in enumerate(strslen) if t==k]

        for i in range(k):
            for j in range(len(strs)):
                if strs[minindex[0]][i]!=strs[j][i]:
                    return strs[0][0:i]

print(solution.prefix(solution,["flower","flow","flight"]))
print(solution.prefix(solution,["dog","racecar","car"]))