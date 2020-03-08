import csv

import numpy as np
import pandas as pd
import requests
import tensorflow as tf

birthdata_url = 'https://raw.githubusercontent.com/nfmcclure/tensorflow_cookbook/master/01_Introduction/07_Working_with_Data_Sources/birthweight_data/birthweight.dat'

birth_weight_file = 'birth_weight.csv'
def csvWrite(distFile):
    '''
    使用PythonI/O写入csv文件
    :param distFile:
    :return:
    '''
    birth_file = requests.get(birthdata_url)
    birth_data = birth_file.text.split('\r\n')
    # split分割函数,以一行作为分割函数，windows中换行符号为'\r\n',每一行后面都有一个'\r\n'符号。
    birth_header = birth_data[0].split('\t')
    # 每一列的标题，标在第一行，即是birth_data的第一个数据。并使用制表符作为划分。
    birth_data = [[float(x) for x in y.split('\t') if len(x) >= 1] for y in birth_data[1:] if len(y) >= 1]
    print(np.array(birth_data).shape)
    # (189, 9)
    # 此为list数据形式不是numpy数组不能使用np,shape函数,但是我们可以使用np.array函数将list对象转化为numpy数组后使用shape属性进行查看。
    with open(distFile, "w", newline='') as f:
        # 其中我们重点需要讲的是 with open(birth_weight_file, "w", newline='') as f: 这个语句。表示写入csv文件,如果不加上参数 newline=''
        # 表示以空格作为换行符，而是用 with open(birth_weight_file, "w") as f: 语句。则生成的表格中会出现空行 with open(birth_weight_file,
        # "w") as f:
        writer = csv.writer(f)
        writer.writerows([birth_header])
        writer.writerows(birth_data)
        f.close()

def readSvc(destFile):
    birth_data = []
    with open(destFile) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        birth_header = next(csv_reader)  # 读取第一行每一列的标题
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)

        birth_data = [[float(x) for x in row] for row in birth_data]  # 将数据从string形式转换为float形式
        birth_data = np.array(birth_data)  # 将list数组转化成array数组便于查看数据结构
        birth_header = np.array(birth_header)
        print(birth_data.shape)  # 利用.shape查看结构。
        print(birth_header.shape)


def pandasRead():
    csv_data = pd.read_csv('birth_weight.csv')  # 读取训练数据
    print(csv_data.shape)  # (189, 9)
    N = 5
    csv_batch_data = csv_data.tail(N)  # 取后5条数据
    print(csv_batch_data.shape)  # (5, 9)
    # 获取2行
    train_batch_data = csv_batch_data.iloc[1, 1]
    print(train_batch_data)
    train_batch_data = csv_batch_data['LOW']  # 取这20条数据的3到5列值(索引从0开始)
    print(train_batch_data)


def tensorflowRead():
    '''
    使用Tensorflow读取csv数据
    '''
    filename = 'birth_weight.csv'
    file_queue = tf.train.string_input_producer([filename])  # 设置文件名队列，这样做能够批量读取文件夹中的文件
    reader = tf.TextLineReader(skip_header_lines=1)  # 使用tensorflow文本行阅读器，并且设置忽略第一行
    key, value = reader.read(file_queue)
    defaults = [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.]]  # 设置列属性的数据格式
    LOW, AGE, LWT, RACE, SMOKE, PTL, HT, UI, BWT = tf.decode_csv(value, defaults)
    # 将读取的数据编码为我们设置的默认格式
    vertor_example = tf.stack([AGE, LWT, RACE, SMOKE, PTL, HT, UI])  # 读取得到的中间7列属性为训练特征
    vertor_label = tf.stack([BWT])  # 读取得到的BWT值表示训练标签

    # 用于给取出的数据添加上batch_size维度，以批处理的方式读出数据。可以设置批处理数据大小，是否重复读取数据，容量大小，队列末尾大小，读取线程等属性。
    example_batch, label_batch = tf.train.shuffle_batch([vertor_example, vertor_label], batch_size=10, capacity=100, min_after_dequeue=10)

    # 初始化Session
    with tf.Session() as sess:
        coord = tf.train.Coordinator()  # 线程管理器
        threads = tf.train.start_queue_runners(coord=coord)
        print(sess.run(tf.shape(example_batch)))  # [10  7]
        print(sess.run(tf.shape(label_batch)))  # [10  1]
        print(sess.run(example_batch)[3])  # [ 19.  91.   0.   1.   1.   0.   1.]
        coord.request_stop()
        coord.join(threads)

    '''
    对于使用所有Tensorflow的I / O操作来说开启和关闭线程管理器都是必要的操作
    with tf.Session() as sess:
        coord = tf.train.Coordinator()  # 线程管理器
        threads = tf.train.start_queue_runners(coord=coord)
        #  Your code here~
        coord.request_stop()
        coord.join(threads)
    '''

if __name__ == '__main__':
    # csvWrite(birth_weight_file)
    # readSvc(birth_weight_file)
    #pandasRead()
    tensorflowRead()