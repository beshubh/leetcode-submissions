class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = sorted([nums1, nums2,], key=len)
        half = (len(nums1) + len(nums2) + 1) // 2
        l, h = 0, len(nums1)
        while l <= h:
            part_x = (l + h) // 2
            part_y = half - part_x
            max_left_x = float('-inf') if part_x == 0 else nums1[part_x - 1]
            min_right_x = float('inf') if part_x >= len(nums1) else nums1[part_x]

            max_left_y = float('-inf') if part_y == 0 else nums2[part_y - 1]
            min_right_y = float('inf') if part_y >= len(nums2) else nums2[part_y]


            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # found mid
                total = len(nums1) + len(nums2)
                if total % 2 == 0:
                    mid = max(max_left_x, max_left_y) + min(min_right_x, min_right_y)
                    return mid / 2
                return float(max(max_left_x, max_left_y))
            elif max_left_x > min_right_y:
                # gone too right 
                h = part_x - 1
            else:
                l = part_x + 1
            

            
