def swap(nums, i, j):
    """
    将第i个元素的值，复制到第i个元素上
    :param nums:
    :param i:
    :param j:
    :return: null
    """
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def duplicate(nums, duplication):
    """
    长度为n的数组里的所有数字都在0到n-1的范围内。查出数组中某个重复的数据
    :param nums:
    :param duplication:
    :return:
    """
    # 1. 非法的数据，则返回false
    if nums is None or len(nums) < 0:
        return False
    # 2.遍历查找第一个重复的数
    for i in range(0, len(nums)):
        while (nums[i] != i):
            # 第i个元素和第i个元素值的位置的值相等
            if nums[i] == nums[nums[i]]:
                duplication.insert(0, nums[i])
                return True
            swap(nums, i, nums[i])


if __name__ == '__main__':
    i = [2, 3, 1, 0, 2, 5, 3]
    temp = []
    duplicate(i, temp)
    print(temp)
