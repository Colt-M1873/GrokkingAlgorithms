# https://leetcode.cn/problems/crawler-log-folder/
# 2022年09月09日 18:54:12

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for item in logs:
            if item=='../':
                count=max(0,count-1)
            elif item == './':
                continue
            else:
                count+=1
        return count