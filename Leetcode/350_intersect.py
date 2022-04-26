import collections


class Solution:
    '''
    def intersect(self, nums1, nums2):
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return num.elements()
    '''  
    def intersect():
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        result = list()

        for num in nums2:
            if num in m.keys():
                result.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        return result

    if __name__ == '__main__':
        print(intersect())
