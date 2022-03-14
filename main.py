# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def lengthOfLIS(self, nums) -> int:
        memo = {}
        end = len(nums) - 1
        memo[end] = 1
        for i in range(end - 1, -1, -1):
            maxSeq = 1
            for j in range(i, end):
                if nums[i] < nums[j + 1]:
                    temp = 1 + memo[j + 1]
                    if temp > maxSeq:
                        maxSeq = temp
            memo[i] = maxSeq
        return max(memo.values())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLIS([0, 1, 0, 3, 2, 3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
