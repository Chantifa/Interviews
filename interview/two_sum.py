def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):  # j starts at i+1 to avoid using same element
            if nums[i] + nums[j] == target:
                return [i, j]

    return []  # No solution found