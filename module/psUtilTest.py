import psutil

__author__ = 'zbcn8'
"""
psutil （ process and system utilities）为cpu 信息监控类
"""
if __name__ == '__main__':
    count = psutil.cpu_count()
    status = psutil.cpu_stats()
    times = psutil.cpu_times()
    memory = psutil.virtual_memory()
    partitions = psutil.disk_partitions()
    print("cpu 数量为：%s" % count)
    print("cpu 状态为：%s" % str(status))
    print("cpu 空闲时间为：%s" % str(times))
    print("内存信息为：%s" % str(memory))
    print("磁盘分区信息为：%s" % str(partitions))
