def bubble_sort(arr):
    """
    冒泡算法
    :return:
    """
    length = len(arr)
    # 第一层遍历(表示比较的次数)
    for i in range(length):
        # 数据处理
        for j in range(1, length - i):
            if arr[j - 1] > arr[j]:
                # 两者交换数据，这里没用temp，因为python 特性： 元组
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr


def bubble_sort_flag(arr):
    """
    带标记的排序算法
    :param arr:
    :return:
    """
    length = len(arr)
    for index in range(length):
        flag = True
        for j in range(1,length-index):
            if arr[j-1] > arr[j]:
                arr[j],arr[j-1] = arr[j-1], arr[j]
                flag = False
        # 表示排序已经完成，则直接退出
        if flag:
            return arr
    return arr

def quick_sort(arr, left, right):
    """
    快速排序
    :param arr:
    :param left:
    :param right:
    :return:
    """
    low = left
    high = right


if __name__ == '__main__':
    arr = [2, 5, 1, 9, 3, 6, 8]
    # arr = bubble_sort(arr)
    arr = bubble_sort_flag(arr)
    print(arr)
