"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log(m + n)).

Example
1:

Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000
Explanation: merged
array = [1, 2, 3] and median is 2.
Example

2:

Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.50000
Explanation: merged
array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array (for efficiency)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while left <= right:
            # Partition indices
            i = (left + right) // 2  # Partition in nums1
            j = half - i  # Partition in nums2

            # Get the four boundary values (use infinity for edge cases)
            maxLeft1 = nums1[i - 1] if i > 0 else float('-inf')
            minRight1 = nums1[i] if i < m else float('inf')
            maxLeft2 = nums2[j - 1] if j > 0 else float('-inf')
            minRight2 = nums2[j] if j < n else float('inf')

            # Check if valid partition found
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Found correct partition
                if total % 2 == 1:
                    # Odd total: median is min of right side
                    return min(minRight1, minRight2)
                else:
                    # Even total: median is average of max(left) and min(right)
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

            elif maxLeft1 > minRight2:
                # Too far right in nums1, move left
                right = i - 1
            else:
                # Too far left in nums1, move right
                left = i + 1

        return 0.0  # Should never reach here

"""
Walkthrough
** Example
1: ** `nums1 = [1, 3], nums2 = [2]

m = 2, n = 1, total = 3, half = 1

Binary search on nums1(smaller array):

Step
1: left = 0, right = 2
i = 1(partition in nums1)
j = 1 - 1 = 0(partition in nums2)

nums1: [1 | 3]
maxLeft1 = 1, minRight1 = 3
nums2: [ | 2]     maxLeft2 = -inf, minRight2 = 2
Is
maxLeft1(1) <= minRight2(2)? Yes ✓
Is
maxLeft2(-inf) <= minRight1(3)? Yes ✓

Valid
partition!
total = 3 is odd
Median = min(minRight1, minRight2) = min(3, 2) = 2.0 ✓


** Example
2: ** `nums1 = [1, 2], nums2 = [3, 4]

m = 2, n = 2, total = 4, half = 2

Step
1: left = 0, right = 2
i = 1
j = 2 - 1 = 1

nums1: [1 | 2]
maxLeft1 = 1, minRight1 = 2
nums2: [3 | 4]
maxLeft2 = 3, minRight2 = 4

Is
maxLeft1(1) <= minRight2(4)? Yes ✓
Is
maxLeft2(3) <= minRight1(2)? No ✗

maxLeft2 > minRight1, need
more
from nums1

left = i + 1 = 2

Step
2: left = 2, right = 2
i = 2
j = 2 - 2 = 0

nums1: [1, 2 |]
maxLeft1 = 2, minRight1 = inf
nums2: [ | 3, 4]  maxLeft2 = -inf, minRight2 = 3

Is
maxLeft1(2) <= minRight2(3)? Yes ✓
Is
maxLeft2(-inf) <= minRight1(inf)? Yes ✓

Valid
partition!
total = 4 is even
Median = (max(2, -inf) + min(inf, 3)) / 2 = (2 + 3) / 2 = 2.5 ✓
Visual Explanation
Finding
median
of[1, 2] and [3, 4]:

We
want
to
split
combined
elements
into
two
equal
halves:

Try
1: [1] | [2]
Left
half
needs
2
elements
[3] | [4]

Left: {1, 3}
Right: {2, 4}
But
3 > 2! Invalid
partition.

Try
2: [1, 2] |
| [3, 4]

Left: {1, 2}
Right: {3, 4}
2 <= 3 ✓  Valid!

Median = (max(1, 2) + min(3, 4)) / 2 = 2.5
"""