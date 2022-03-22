# https://leetcode.com/problems/remove-duplicate-letters/
# 2022 3.18


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # failed
        # v1 copied, brilliant 
        # https://leetcode.com/problems/remove-duplicate-letters/discuss/889477/Python-O(n)-greedy-with-stack-explained 
        # Let us try to build our answer in greedy way: we take letter by letter and put them into stack: if we have next letter which decreased lexicographical order of string, we remove it from stack and put new letter. However we need to be careful: if we remove some letter from stack and it was the last occurence, then we failed: we can not finish this process. So, we need to do the following:

        # Find last_occ: last occurences for each letter in our string
        # Initialize our stack either as empty or with symbol, which is less than any letter ('!' in my case), so we do not need to deal with the case of empty stack. Also initialize Visited as empty set.
        # Iterate over our string and if we already have symbol in Visited, we just continue.
        # Then, we try to remove elements from the top of our stack: we do it, if new symbol is less than previous and also if last occurence of last symbol is more than i: it means that we have removed symbol later in our string, so if we remove it we will not fail to constract full string.
        # Append new symbol to our stack and mark it as visited.
        # Finally, return string built from our stack.
        
        last_occ = {c: i for i, c in enumerate(s)}
        stack = ["!"]
        Visited = set()
        
        for i, symbol in enumerate(s):
            if symbol in Visited: continue
            
            while (symbol < stack[-1] and last_occ[stack[-1]] > i):
                Visited.remove(stack.pop())
            stack.append(symbol)
            Visited.add(symbol)        
        return "".join(stack)[1:]