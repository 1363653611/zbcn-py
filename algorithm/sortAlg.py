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
        for j in range(1, length - index):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                flag = False
        # 表示排序已经完成，则直接退出
        if flag:
            return arr
    return arr


def quick_sort(arr):
    """
    快速排序
    1. 从数列中挑出一个元素，称为”基准”（pivot），
    2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
    3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    :param arr:
    :param left:
    :param right:
    :return:
    """
    # 比基准小的数组
    less = []
    # 比基准大的数组
    more = []
    # 等于基准数据的集合
    pivotList = []

    # 跳出递归的节点
    if len(arr) <= 1:
        return arr
    else:
        # 将第一个值作为基准节点
        pivote = arr[0]
        for i in arr:
            # 将 比基准小的放到 less 数组
            if i < pivote:
                less.append(i)
            elif i > pivote:  # 比基准大的放到more 节点
                more.append(i)
            else:  # 等于基准的放到 pivoteList
                pivotList.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        #  最终结果拼接
        return less + pivotList + more


def quick_sort2(arr, left, right):
    """
    1. 快排需要将序列变成两个部分，就是「序列左边全部小于一个数」，「序列右面全部大于一个数」，
    然后利用递归的思想再将左序列当成一个完整的序列再进行排序，同样把序列的右侧也当成一个完整的序列进行排序。
    2. 其中这个数在这个序列中是可以随机取的，可以取最左边，可以取最右边，当然也可以取随机数。但是「通常」不优化情况我们取最左边的那个数
    :param arr:  原始数组
    :param left: 起始位置:默认 0
    :param right: 数组的长度 -1
    :return:
    """
    low = left
    high = right
    if low > high:  # 下面两句的顺序一定不能混，否则会产生数组越界！
        return
    # 额外空间temp，取最左侧的一个作为衡量，最后要求左侧都比它小，右侧都比它大。
    temp = arr[low]
    # 这一轮要求把左侧小于temp,右侧大于temp。
    while low < high:
        # 右侧找到第一个小于temp的停止
        while low < high and arr[high] > temp:
            high -= 1
        arr[low] = arr[high]
        # 左侧找到第一个大于 temp 的值停止
        while low < high and arr[low] < temp:
            low += 1
        arr[high] = arr[low]

    # 赋值然后左右递归分治求之
    arr[low] = temp
    quick_sort2(arr, left, low - 1)
    quick_sort2(arr, low + 1, right)


def insert_sort(arr):
    """
    快速排序
    1. 选取当前位置(当前位置前面已经有序) 目标就是将当前位置数据插入到前面合适位置。
    2. 向前枚举或者二分查找，找到待插入的位置。
    3. 移动数组，赋值交换，达到插入效果。
    :param arr:
    :return:
    """
    length = len(arr)
    if length == 0:
        return
    for i in range(1, length):
        temp = arr[i]  # 取第二个值为当前值
        for j in range(i - 1, -1, -1):  # 循环 i-1 个元素
            if arr[j] > temp:  # 如果 比 temp 大，则 将arr[j] 赋值给 arr[j+1], arr[j] 赋值为temp
                arr[j + 1], arr[j] = arr[j], temp
                print(arr)  # 打印当前需要排序的数组
            else:  # j 前面的数据都是排好序的，所以，只要arr[j]比 temp小，则 j-- 都比 temp 小
                break


def insert_sort2(arr):
    """
    1. 从第一个元素开始，该元素可以认为已经被排序
    2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
    3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
    4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5. 将新元素插入到该位置后
    6. 重复步骤2~5
    :param arr:
    :return:
    """
    length = len(arr)
    if length == 0:
        return
    for i in range(1, length):
        # 后一个元素和前一个元素比较
        # 如果比前一个小
        if arr[i] < arr[i - 1]:
            # 将这个数取出
            temp = arr[i]
            index = 1  # 保存下标
            # 从后往前依次比较每个元素
            for j in range(i - 1, -1, -1):
                # 和比取出元素大的元素交换
                if arr[j] > temp:
                    arr[j + 1] = arr[j]
                    index = j
                else:
                    break
            # 插入元素
            arr[index] = temp


def shell_sort(arr):
    """
    希尔排序:
    1. 计算初始步长 (arr的长度除于 2)
    2. 当步长 大于 1时,循环处理
    3. 以步长为初始值,结束值为数组的长度,循环arr
    4. 当 当前值 i - d 大于 等于 0时,按照插入法 排序 步长为 d 的数据
    5. 修改步长
    :param arr:
    :return:
    """
    length = len(arr)  # 数组的长度
    # 初始的步长 ('//' 整除,返回整数结果)
    d = length // 2
    while d >= 1:  # 当步长 大于等于 1 时
        for i in range(d, length, 1):
            temp = arr[i]
            j = i - d
            while j >= 0:  # 按照指定的步长将数据按照插入法排序
                if arr[j] > temp:
                    arr[j + d] = arr[j]
                    arr[j] = temp
                j -= d
        d //= 2  # 步长再次折半


def shell_sort2(arr):
    """
    1.选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
    2.按增量序列个数k，对序列进行k 趟排序；
    3.每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
    :param arr:
    :return:
    """
    length = len(arr)
    # 增量序列计算逻辑
    h = 1
    while h < length // 3:
        h = 3 * h + 1
    # 如果增量序列大于 1
    while h >= 1:
        # 以增量序列为开始，对数组进行排序
        for i in range(h, length - 1, 1):
            j = i
            # 对截取数据按照 步长 h 进行排序
            while j >= h:
                if arr[j] < arr[j - h]:
                    arr[j - h], arr[j] = arr[j], arr[j - h]
                j -= h
        # 调整增量大小
        h = h // 3


def selection_sort(arr):
    """
    选择排序
    1. 在未排序序列中找到最小（最大）元素，存放到排序序列的起始位置
    2. 然后再从剩余的未排序序列中继续寻找最小（最大）元素，然后放到已排序序列的末尾
    3.重复第二步，直到所有元素排序完成
    :param arr:
    :return:
    """
    length = len(arr)

    for i in range(0, length):
        min = i
        for j in range(i + 1, length):
            if arr[j] < arr[min]:
                min = j
                arr[min], arr[i] = arr[i], arr[min]
    return arr


def selection_sort2(arr):
    length = len(arr)
    for i in range(0, length):
        min = i
        temp = arr[i]
        # 找出最小元素的 索引值
        for j in range(i + 1, length):
            if arr[j] < arr[min]:
                min = j
        # temp = arr[i]
        # arr[i] = arr[min]
        # arr[min] = temp
        arr[i], arr[min] = arr[min], temp
    return arr


def heap_sort(arr):
    # 创建最大堆
    for start in range((len(arr) - 2) // 2, -1, -1):
        shift_down(arr, start, len(arr) - 1)
        print('第一次：%s' % arr)
    # 堆排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        print('排序后调整前：%s' % arr)
        shift_down(arr, 0, end - 1)
        print('堆排序后调整后：%s' % arr)
    return arr


def shift_down(arr, start, end):
    """
    最大堆调整
    :param arr:
    :param start:
    :param end:
    :return:
    """
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def merger_sort(arr):
    """
    归并排序:
    ①进行两两归并使记录关键字有序，
    ②得到 n/2 个长度为 2 的有序子表；
    ③重复第②步直到所有记录归并成一个长度为 n 的有序表为止。
    此算法的实现不像图示那样简单，现分三步来讨论。首先从宏观上分析，首先让子表表长 L=1 进行处理；
    不断地使 L=2*L ，进行子表处理，直到 L>=n 为止，把这一过程写成一个主体框架函数 mergesort 。
    :param arr:
    :return:
    """
    # sort(arr, 0, len(arr) - 1)
    sort2(arr)


def sort2(arr):
    """
    非递归方式
    :param arr:
    :return:
    """
    length = len(arr)
    # 步长
    step = 2
    while step <= length:
        i = 0  # 起始位置
        while (step + i) <= length:
            curr_length = i + step
            center = i + step // 2 - 1
            merge(arr, i, center, curr_length - 1)
            i += step
        # 处理末尾残余部分
        merge(arr, i, i + step // 2 - 1, length - 1)
        # 调整步长
        step *= 2
    # 最后再从头处理一遍
    merge(arr, 0, step // 2 - 1, length - 1)


def sort(arr, left, right):
    """
    采用递归方式排序
    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return
    # 找出中间索引
    center = (left + right) // 2
    # 对左边数组进行递归
    sort(arr, left, center)
    # 对右边数组进行递归
    sort(arr, center + 1, right)
    #  合并
    merge(arr, left, center, right)


def merge(arr, left, center, right):
    """
    合并操作
    :param arr: 数组对象
    :param left: 左数组的第一个元素的索引
    :param center: 左数组的最后一个元素的索引, center+1 是右数组的第一个元素的索引
    :param right: 右数组的最有一个元素的索引
    :return:
    """
    # 临时数组
    temp_arr = [None] * len(arr)
    # 右数组第一个元素的索引
    mid_new = center + 1
    # third 记录临时数组的索引
    third = left
    # 缓存左侧数组第一个元素的索引
    temp = left
    while left <= center and mid_new <= right:
        # 从两个数组中取出最小的放到临时数组中
        if arr[left] <= arr[mid_new]:
            temp_arr[third] = arr[left]
            left += 1
        else:
            temp_arr[third] = arr[mid_new]
            mid_new += 1
        third += 1

    # 剩余部分依次放入临时数组(以下两个 while 实际上只会执行一个)
    while mid_new <= right:
        temp_arr[third] = arr[mid_new]
        third += 1
        mid_new += 1
    while left <= center:
        temp_arr[third] = arr[left]
        left += 1
        third += 1
    # 将临时数组中的内容拷贝回原数组(原 left - right 范围内的内容被拷贝回原数组)
    while temp <= right:
        arr[temp] = temp_arr[temp]
        temp += 1

    print('合并后:%s' % arr)


def count_sort(arr):
    """
    计数排序:
    1. 找出待排序的数组中最大和最小的元素
    2. 统计数组中每个值为i的元素出现的次数，存入数组 C 的第 i 项
    3. 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
    4. 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
    :param arr:
    :return:
    """
    max = 0
    min = 1000
    # 获取最大值和最小值
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    # 创建数组C
    count_length = max - min + 1
    count = [0] * count_length
    for index in arr:
        count[index - min] += 1
    index = 0
    # 添值
    # 循环 max-min+ 1 次(即:count 的数组长度次)
    for a in range(count_length):
        for c in range(count[a]):  # 填充 count[a] > 0 的值, 而且循环 count[a] 次
            # 值为  a + min
            arr[index] = a + min
            index += 1
    return arr


def bucket_sort(arr, bucket_size):
    """
    桶排序
    1.设置一个定量的数组当作空桶子。
    2.寻访序列，并且把项目一个一个放到对应的桶子去。
    3.对每个不是空的桶子进行排序。
    4.从不是空的桶子里把项目再放回原来的序列中。
    :param arr:
    :param bucket_size:
    :return:
    """
    if len(arr) == 0:
        return arr
    min = arr[0]
    max = arr[0]
    # 获取原始数据中的最大值和最小值
    for item in arr:
        if item < min:
            min = item
        elif item > max:
            max = item
    # 初始化桶
    default_bucket_size = 5  # 桶的初始化大小为 5
    # 桶的最终大小
    bucket_size = bucket_size or default_bucket_size
    # 桶的数量
    bucket_count = (max - min) // bucket_size + 1
    # 创建空桶
    buckets = [[] * bucket_size for _ in range(bucket_count)]
    # 利用映射函数将数据分配到各个桶中
    for i in range(len(arr)):
        index = (arr[i] - min) // bucket_size
        buckets[index].append(arr[i])

    # 清空原始数组
    arr.clear()
    # 对每个桶进行插入排序
    for bucket in buckets:
        insert_sort(bucket)  # 插入排序
        # 将排序好的 数据插入到 arr中
        for item in bucket:
            arr.append(item)
    return arr


def bucket_sort2(arr):
    max_value = arr[0]
    min_value = arr[0]
    # 获取最大值和最小值
    for i in arr:
        min_value = min(i, min_value)
        max_value = max(i, max_value)
    print('最大值: %s' % max_value)
    print('最小值:%s' % min_value)

    # 计算 桶的数量
    bucket_num = (max_value - min_value) // len(arr) + 1
    # 创建桶
    buckets = [[] for _ in range(bucket_num)]
    # 将每个元素按照一定的规则放到对应的桶中
    for i in range(len(arr)):
        # 桶的位置 index = (当前值-最小值)除以 数组长度 求整
        index = (arr[i] - min_value) // len(arr)
        buckets[index].append(arr[i])

    # 将原始数组清空
    arr.clear()
    # 对每个桶中的元素排序
    # 将桶中的元素放到原始数组
    for bucket in buckets:
        bubble_sort(bucket)
        for item in bucket:
            arr.append(item)
    return arr


def max_bit(arr, n):
    """
    辅助函数,求数数组中元素的最大位数
    :param arr:
    :param n: 数组的长度
    :return:
    """
    # 求出最大值
    max_value = arr[0]
    # 获取最大值和最小值
    for i in arr:
        max_value = max(i, max_value)
    # 求位数
    d = 1  # 位数,默认为1
    precision = 10  # 精度
    while max_value >= precision:
        max_value //= 10
        d += 1
    return d


def radix_sort(arr):
    """
    基数排序
    1. 取得数组中的最大数，并取得位数；
    2. arr为原始数组，从最低位开始取每个位组成radix数组；
    3. 对radix进行计数排序（利用计数排序适用于小范围数的特点）
    :param arr:
    :return:
    """
    length = len(arr)
    # 最大位数
    d = max_bit(arr, length)
    temp = [0] * length
    # count 为 10 的数组,原因是10进制
    count = [0] * 10  # 计数器
    radix = 1
    # 进行 d次排序
    for i in range(1, d + 1):
        # 每次分派前清空计数器
        for j in range(10):
            count[j] = 0
        for j in range(length):
            # 统计每个桶中的记录数
            k = (arr[j] // radix) % 10
            count[k] += 1
        # 将各个桶中的数字个数，转化成各个桶中最后一个数字的下标索引
        for j in range(1, 10):
            # 将temp 中的位置依次分配给每个桶
            count[j] = count[j - 1] + count[j]
        # 将所有桶中记录依次放到temp中
        for j in range(length - 1, -1, -1):
            k = (arr[j] // radix) % 10
            temp[count[k] - 1] = arr[j]
            count[k] -= 1

        # 将临时数组的内容复制到 arr中
        for j in range(0, length, 1):
            arr[j] = temp[j]
        radix = radix * 10
    temp.clear()
    count.clear()
    return arr


def item_len(item):
    """
    计算一个数字共有多少位
    :param item:
    :return:
    """
    d = 1  # 位数,默认为1
    precision = 10  # 精度
    while item >= precision:
        item %= 10
        d += 1
    return d


def max_lenght(arr):
    """
    一个数组中,最大数的位数
    :param arr:
    :return:
    """
    max_len = 0
    length = len(arr)
    for i in range(length):
        current_len = item_len(arr[i])
        max_len = max(current_len, max_len)
    return max_len


def get_digit(x, d):
    """
    获取 x 这个数的 d 位数上的数字
     比如获取 123 的 0 位数,结果返回 3
    :param x:
    :param d:
    :return:
    """
    a = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
    # 求商 取余
    return (x // a[d]) % 10


def do_radix_sort(arr, digit, max_len):
    """
    基数排序的核心算法
    :param arr:
    :param digit:
    :param max_len:
    :return:
    """
    if digit > max_len:
        return arr
    radix = 10  # 基数
    arr_len = len(arr)
    # 计数 arr中元素的个数(计数法)
    count = [0] * radix
    # 桶,存放元素
    bucket = [0] * arr_len
    #  统计将数组中的数字分配到桶中后，各个桶中的数字个数
    for i in range(arr_len):
        # 每一位的数字
        digit_data = get_digit(arr[i], digit)
        count[digit_data] += 1
    # 将各个桶中的数字个数，转化成各个桶中最后一个数字的 "下标索引"
    for i in range(1, radix):
        count[i] = count[i] + count[i - 1]
    #  将原数组中的数字分配给辅助数组 bucket
    for j in range(arr_len - 1, 0, -1):
        num = arr[j]
        d = get_digit(num, digit)
        bucket[count[d] - 1] = num
        count[d] -= 1

    return do_radix_sort(bucket, digit + 1, max_len)


def radix_sort2(arr):
    """
    基数排序
    :param arr:
    :return:
    """
    length = len(arr)
    if length == 0:
        return arr
    # 数组中元素的最大位数
    max_len = max_lenght(arr)

    return do_radix_sort(arr, 0, max_len)


if __name__ == '__main__':
    arr = [2, 5, 1, 9, 3, 6, 8, 6, 6]
    # 冒泡排序
    # arr = bubble_sort(arr)
    # arr = bubble_sort_flag(arr)
    # 快速排序
    # arr = quick_sort(arr)

    # quick_sort2(arr, 0, len(arr) - 1)

    # insert_sort(arr)
    # shell_sort(arr)
    # shell_sort2(arr)
    # selection_sort(arr)
    # selection_sort2(arr)
    # heap_sort(arr)
    # merger_sort(arr)
    # count_sort(arr)
    # arr = bucket_sort(arr, 3)
    # bucket_sort2(arr)

    arr = [2314, 5428, 373, 2222, 17]
    # arr = radix_sort2(arr)
    arr = radix_sort(arr)

    print(arr)
