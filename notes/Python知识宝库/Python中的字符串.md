# <font id=top>Python中的字符串</font>

[TOC]

## 前言
现实生活中文字随处可见，编程语言中则用字符串来表示，字符串是Python中最常用的数据类型。想想在没有图形化界面的时代，几乎都是对字符串和数字的处理，衍生到后来的网页、Windows应用程序等都能看到对字符串的操作。还有每个国家都有不同的语言，而字符串有不同的字符串编码来表示。越容易小瞧的反而越重要

<br/>

## 英语词汇表

| 单词     | 中文解释                          |                全 称                 |
| :------- | :-------------------------------- | :----------------------------------: |
| UTF-8    | 针对Unicode的一种可变长度字符编码 | Unicode Transformation Format(8位元) |
| builtins | 内置模块                          |                  \                   |
| format   | 格式、使格式化                    |                  \                   |



## 一、字符串编码

由于 Python 源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为<font color='#FF0059'> UTF-­8 编码</font>。当 Python 解释器读取源代码时，为了让它按 UTF-­8 编码读取，我们通常在文件开头写上这两行： 

![](./assets/指定编码格式.PNG)

```python
# !/usr/bin/env python
# -*- coding:utf-8 -*-
```

第一行注释是为了告诉 <font color='#FF0059'>Linux/OS X 系统，这是一个 Python 可执行程序</font>，Windows 系统会忽略这个注释； 

第二行注释是为了告诉<font color='#FF0059'> Python 解释器，按照 UTF­-8 编码读取源代码</font>，否则，你在源代码中写的中文输出可能会有乱码。我个人建议在每个Python文件中都写上这两行。



## 二、字符串简单的使用

### 2.1 用print()打印字符串。

在Python中可以通过<font color='#FF0059'>英文</font>的  (双引号<font color='#FF0059' size='5em'>"</font>)  或者  (单引号<font color='#FF059' size='5em'>'</font>)  识别出字符串来

```python
content1 = 'hello world --- Python'
content2 = "hello world --- Java"

print(content1)
print(content2)
```

### 2.2 如果想在字符中显示(双引号<font color='#FF0059' size='5em'>"</font>)  或者  (单引号<font color='#FF059' size='5em'>'</font>) 怎么办呢？

   #### 	2.2.1 单、双引号一起用

```python
content3 = "Let's go"
content4 = '小明同学打乒乓球把玻璃给弄碎了，他是真的"很厉害"'
	
print(content3)
print(content4)
```
<br/>
   #### 	2.2.2使用转义字符 <font color='#FF0590'>\\</font>

``` python
content5 = "C、Html、JavaScript、Css、\"Python\"、Java、Markdown"
content6 = 'My name is \'Hui\'!'
print(content5)
print(content6)
```

结果：

C、Html、JavaScript、Css、\"Python\"、Java、Markdown

My name is 'Hui'!

<br/>

### 2.3 中文的(单引号<font color='#FF059' size='5em'>‘</font>)、(双引号<font color='#FF0059' size='5em'>“</font>) 

然而在我们<font color='#FF059'>博大精深的中华文化</font>当中， (单引号<font color='#FF059' size='5em'>‘</font>)、(双引号<font color='#FF0059' size='5em'>“</font>)  可以表示

​	**1. 引号可表示引用 **
​	**2. 表示特定称谓**
​	**3. 表示特殊含义**
​	**4. 表示讽刺和嘲笑以及突出强调**

```python 
content7 = "“怕什么！海的美就在这里！”我说道"
content8 = '现代画家徐悲鸿笔下的马，正如有的评论家所说的那样，“形神兼备，充满生机”。'
content9 = "他们（指友邦人士）维持他们的“秩序”的监狱，就撕掉了他们的“文明”的面具。"

print(content7)
print(content8)
print(content9)
```

<font color='red'>注意：在字符串中使用中文的(单引号<font color='#FF059' size='5em'>‘</font>)、(双引号<font color='#FF0059' size='5em'>“</font>)不需要用转义字符\\</font>

<br/>

### 2.4 运算符操作字符串

```python
# 运算符操作字符串
print('5' + '3')    # --> '53'	拼接
print('--' * 20 + '分割线' + '--' * 20)	# '--' * 20 等同于20个'--'相加拼接

# 字符串累加
result = ''
for i in range(10):
    result += str(i)
print(result)   # -->'0123456789'
```

<br/>

## 三、字符串格式化

在 Python 中，采用的格式化方式和 C 语言是一致的，用<font color='#FF059' size='5em'>%</font>实现，如下：

| 格式   | 含义                                                 |
| ------ | ---------------------------------------------------- |
| %c     | 单字符 (整数[ASCII值]或者长度为1的字符)              |
| %r     | 字符串 (通过repr()进行转换)                          |
| %s     | 字符串 (通过str()进行转换)                           |
| %d或%i | 整型占位符                                           |
| %u     | 无符号的十进制整数                                   |
| %o     | 无符号的八进制整数                                   |
| %x或%X | 无符号的十六进制整数                                 |
| %e或%E | 指数符号(科学计数法)                                 |
| %f或%F | 浮点数(默认6位小数，四舍五入)                        |
| %g或%G | 如果指数大于-4或者小于-4精度值则和%e、%E、%f、%F相同 |

你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s 表示用字符串替换， %d 表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只 有一个%?，括号可以省略。 常见的占位符有： %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数 其中，格式化整数和浮点数还可以指定是否补 0 和整数与小数的位数： >>> '%2d-%02d' % (3, 1) ' 3-01' >>> '%.2f' % 3.1415926 '3.14' 

如果你不太确定应该用什么，%s 永远起作用，它会把任何数据类型转换为字符串： 

<br/>

## 四、字符串的方法

由于字符串在编程中经常用到，因此Python对字符串的操作有非常多的方法。

### 4.1 dir()查看str的所有方法

我们可以用内置模块(builtins.py)的<font color='#FF059'>dir()函数</font>来查看某个的类的所有方法，返回的是所有方法汇总的列表(list) 

```Python
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


def main():
    content = 'Hello World --- Python'
    print(content)

    # 查看字符串类的所有方法
    print(dir(str))

    # 在一行上看不全且看的累，我们微调一下
    print('--' * 50)
    print('  '*20 + 'str类的所有方法(%d)' % len(dir(str)) + '  '*20)
    print('--' * 50)
    list_out(dir(str), row_num=5)
  	


if __name__ == '__main__':
    main()
```



```text
-----------------------------------------------------------------------------------------
                                    str类的所有方法(76)                                     
-----------------------------------------------------------------------------------------
__add__           __class__         __contains__      __delattr__       __dir__       

__doc__           __eq__            __format__        __ge__            __getattribute__  
__getitem__       __getnewargs__    __gt__            __hash__          __init__          
__iter__          __le__            __len__           __lt__            __mod__   

__mul__           __ne__            __new__           __reduce__        __reduce_ex__  

__repr__          __rmod__          __rmul__          __setattr__       __sizeof__        
__str__           __subclasshook__  capitalize        casefold          center            
count             encode            endswith          expandtabs        find              
format            format_map        index             isalnum           isalpha   

isdecimal         isdigit           isidentifier      islower           isnumeric  

isprintable       isspace           istitle           isupper           join              
ljust             lower             lstrip            maketrans         partition   

replace           rfind             rindex            rjust             rpartition        
rsplit            rstrip            split             splitlines        startswith        
strip             swapcase          title             translate         upper      

zfill

```

我们可以看到总共有<font color='#FF059' size='5em'>76</font>个方法，魔术方法<font color='#FF059' size='5em'>32</font>个，普通方法<font color='#FF059' size='5em'>44</font>个

魔术方法（magic method）是特殊方法的昵称，在Python中的特殊方法，一般都是使用诸如`__xxx__`（前后两个下划线，中间是方法名）的命名方式，例如：`__init__`、`__class__`。

在Python中，要拿到一个集合的某个元素，可以使用对应的引索进行取值，比如`list[key]`，这背后利用的是`__getitem__`方法，为了拿到`my_list[key]`的值，Python解释器实际上会调用`my_list.__getitem__(key)`。

Python也是面向对象编程语言，对于求一个集合的长度使用`len(list)`而不是`list.len()`，背后就是特殊方法的作用，调用了`list.__len__()`方法，和面向对象完全符合，而且还起到简化的作用，变得更加通俗易懂,这就是Python的简洁体现之一。

参考链接：https://blog.csdn.net/u012581234/article/details/80925459

<br/>

### 4.2 使用help()来查看方法、函数的文档

```python
help(list_out)

输出结果:
Help on function list_out in module __main__:

list_out(out_list, row_num) -> (<class 'list'>, <class 'int'>)
    列表输出
    :param out_list: 待输出的列表
    :param row_num: 一行输出多少个
    :return:
        
help(str.split)

输出结果:
Help on method_descriptor:

split(...)
    S.split(sep=None, maxsplit=-1) -> list of strings
    
    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.
```

<font color='red'>注意：使用help()时不要把函数、方法的括号()写进去,否则报错</font>

<br/>

### 4.3 字符串常用方法

| 方法名                      | 功能                   |
| --------------------------- | ---------------------- |
| upper()、lower()            | 把字符串转成大、小写   |
| split()                     | 字符串切割             |
| startswith()、endswith()    | 字符串前、尾部比较     |
| replace()                   | 字符串替换             |
| strip()、lstrip()、rstrip() | 去除空格               |
| find()                      | 在字符串中查找子字符串 |

<br/>

## 五、索引、切片操作字符串

。。。

<br/>