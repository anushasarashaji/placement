#https://leetcode.com/problems/backspace-string-compare/
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def loop(str):
#             st=[]
#             for i in str:
#                 if i=="#":
#                     if st:
#                         st.pop()
#                 else:
#                     st.append(i)
#             w="".join(st)
#             return w
#         str1=loop(s)
#         str2=loop(t)
#         if str1==str2:
#             return True
#         else:
#             return False

#https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for i in range(len(nums1)):
        ind = nums2.index(nums1[i])
        max = nums1[i]
        flag = 0
        for j in range(ind + 1, len(nums2)):
            if nums2[j] > max:
                max = nums2[j]
                flag = 1
                break
        if flag == 0:
            max = -1
        ans.append(max)
    return ans