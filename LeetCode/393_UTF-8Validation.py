# https://leetcode.com/problems/utf-8-validation/
# 2022年09月13日 22:02:25

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # v1 ugly
        i=0
        while i<len(data):
            # print(bin(data[i]))
            if data[i]>>7==0:
                i+=1
                # print(0)
            elif data[i]>>5==0b110:
                # print(110)
                if i+1<len(data) and data[i+1]>>6==0b10:
                    i+=2
                else:
                    return False
            elif data[i]>>4==0b1110:
                # print(1110)
                if i+2<len(data) and data[i+1]>>6==0b10 and data[i+2]>>6==0b10:
                    i+=3
                else:
                    return False
            elif data[i]>>3==0b11110:
                # print(1110)
                if i+3<len(data) and data[i+1]>>6==0b10 and data[i+2]>>6==0b10 and data[i+3]>>6==0b10 :
                    i+=4
                else:
                    return False
            else:
                return False
        return True