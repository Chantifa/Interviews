import java.util.ArrayList;
import java.util.List;

public class MinimumPairRemoval {
    /**
     * Given an array nums, you can perform the following operation any number of times:
     * <p>
     * Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
     * Replace the pair with their sum.
     * Return the minimum number of operations needed to make the array non-decreasing.
     * <p>
     * An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
     * <p>
     * <p>
     * <p>
     * Example 1:
     * <p>
     * Input: nums = [5,2,3,1]
     * <p>
     * Output: 2
     * <p>
     * Explanation:
     * <p>
     * The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
     * The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
     * The array nums became non-decreasing in two operations.
     * <p>
     * Example 2:
     * <p>
     * Input: nums = [1,2,2]
     * <p>
     * Output: 0
     * <p>
     * Explanation:
     * <p>
     * The array nums is already sorted.
     * <p>
     * <p>
     * <p>
     * Constraints:
     * <p>
     * 1 <= nums.length <= 50
     * -1000 <= nums[i] <= 1000
     */

    class Solution {
        public int minimumPairRemoval(int[] nums) {
            // Convert to ArrayList for easier manipulation
            List<Integer> list = new ArrayList<>();
            for (int num : nums) {
                list.add(num);
            }

            int operations = 0;

            while (!isNonDecreasing(list)) {
                // Find adjacent pair with minimum sum (leftmost if ties)
                int minSum = Integer.MAX_VALUE;
                int minIdx = 0;

                for (int i = 0; i < list.size() - 1; i++) {
                    int pairSum = list.get(i) + list.get(i + 1);
                    if (pairSum < minSum) {
                        minSum = pairSum;
                        minIdx = i;
                    }
                }

                // Replace the pair with their sum
                list.set(minIdx, minSum);
                list.remove(minIdx + 1);
                operations++;
            }

            return operations;
        }

        private boolean isNonDecreasing(List<Integer> list) {
            for (int i = 1; i < list.size(); i++) {
                if (list.get(i) < list.get(i - 1)) {
                    return false;
                }
            }
            return true;
        }
    }
}
