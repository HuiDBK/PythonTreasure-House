# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
详细理解字符串
字符串的一系列操作
author:Mr Liu
version:1.0
"""


def list_out(out_list, row_num)-> (list, int):
    """
    列表输出
    :param out_list: 待输出的列表
    :param row_num: 一行输出多少个
    :return:
    """
    for index in range(len(out_list)):
        print(out_list[index].ljust(18), end='')
        if (index+1) % row_num == 0:
            print()


def simple_str_use():
    """
    简单字符串的使用
    """
    print('--'*50)
    print('  '*20 + '简单字符串的使用Demo' + '  '*20)
    print('--' * 50)
    content1 = 'Hello World --- Python'
    content2 = 'Hello World --- Java'
    content3 = "Let's go"
    content4 = '小明同学打乒乓球把玻璃给弄碎了，他是真的"很厉害"'
    content5 = "C、Html、JavaScript、Css、\"Python\"、Java、Markdown"
    content6 = 'My name is \'Hui\'!'
    content7 = "“怕什么！海的美就在这里！”我说道"
    content8 = '现代画家徐悲鸿笔下的马，正如有的评论家所说的那样，“形神兼备，充满生机”。'
    content9 = "他们（指友邦人士）维持他们的“秩序”的监狱，就撕掉了他们的“文明”的面具。"

    contents = [content1, content2, content3, content4, content5,
                content6, content7, content8, content9]
    list_out(contents, row_num=1)

    # 运算符操作字符串
    print('5' + '3')  # --> '53'	拼接
    print('--' * 20 + '分割线' + '--' * 20)  # '--' * 20 等同于20个'--'相加拼接
    # 字符串累加
    result = ''
    for i in range(10):
        result += str(i)
    print(result)   # -->'0123456789'
    print()


def str_method_demo():
    """
    字符串常用方法
    """
    print('--' * 50)
    print('  ' * 20 + '字符串常用方法Demo' + '  ' * 20)
    print('--' * 50)

    # 查看字符串类的所有方法
    # print(dir(str))
    # 在一行上看不全且看的累，我们微调一下
    print('--' * 50)
    print('  ' * 20 + 'str类的所有方法(%d)' % len(dir(str)) + '  ' * 20)
    print('--' * 50)
    list_out(dir(str), row_num=5)
    print()

    # 使用help()查看文档
    help(list_out)
    help(str.split)


def str_format_demo():
    """
    格式化字符串
    """
    pass


def str_index_demo():
    """
    索引、切片操作字符串
    """
    pass


def main():
    # 简单字符串的使用
    simple_str_use()

    # 字符串常用方法
    str_method_demo()

    # 格式字符串
    str_format_demo()

    # 用切片操作字符串
    str_index_demo()

    print('%f' % 3.1415926)


if __name__ == '__main__':
    main()