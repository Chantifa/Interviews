"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Prev
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


"""

## Walkthrough

** Input: ** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
`
Index: 0
1
2
3
4
5
6
7
8
Height: 1
8
6
2
5
4
8
3
7

Step
1: left = 0, right = 8
height[0] = 1, height[8] = 7
area = 8 × min(1, 7) = 8 × 1 = 8
Move
left(1 < 7)

Step
2: left = 1, right = 8
height[1] = 8, height[8] = 7
area = 7 × min(8, 7) = 7 × 7 = 49 ← MAX
Move
right(8 > 7)

Step
3: left = 1, right = 7
height[1] = 8, height[7] = 3
area = 6 × min(8, 3) = 6 × 3 = 18
Move
right(8 > 3)

Step
4: left = 1, right = 6
height[1] = 8, height[6] = 8
area = 5 × min(8, 8) = 5 × 8 = 40
Move
right(equal, either
works)

Step
5: left = 1, right = 5
height[1] = 8, height[5] = 4
area = 4 × min(8, 4) = 4 × 4 = 16
Move
right

Step
6: left = 1, right = 4
height[1] = 8, height[4] = 5
area = 3 × min(8, 5) = 3 × 5 = 15
Move
right

Step
7: left = 1, right = 3
height[1] = 8, height[3] = 2
area = 2 × min(8, 2) = 2 × 2 = 4
Move
right

Step
8: left = 1, right = 2
height[1] = 8, height[2] = 6
area = 1 × min(8, 6) = 1 × 6 = 6
Move
right

Step
9: left = 1, right = 1 → STOP(left
not < right)

max_area = 49 ✓

## Visual
|
8 |   █           █
7 |   █           █   █
6 |   █   █       █   █
5 |   █   █   █   █   █
4 |   █   █   █ █ █   █
3 |   █   █   █ █ █ █ █
2 |   █   █ █ █ █ █ █ █
1 | █ █   █ █ █ █ █ █ █
└──────────────────────
0
1
2
3
4
5
6
7
8

Best
container: between
index
1 and 8
Width = 7, Height = 7, Area = 49
"""