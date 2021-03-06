# 实现strStr()


#### 一、题目

实现 **strStr()** 函数。

给定一个```haystack```字符串和一个```needle```字符串，在```haystack```字符串中找出```needle```字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

* 示例 1:
```
输入: haystack = "hello", needle = "ll"
输出: 2
```
* 示例 2:
```
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```
* 说明:

当```needle```是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。对于本题而言，当```needle```是空字符串时我们应当返回**0**。这与C语言的 **strstr()** 以及Java的 **indexOf()** 定义相符。


#### 二、Python3程序
```python
# -*- coding：utf-8 -*-
# &Author  AnFany

# 28_Implement_strStr()  实现strStr()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle为空，返回0
        if not needle:
            return 0
        # haystack为空，返回-1
        if not haystack:
            return -1

        length_needle = len(needle)

        length_haystack = len(haystack)

        for h in range(length_haystack - length_needle + 1):
            if haystack[h] == needle[0]:  # 如果与needle的首字母相同
                if haystack[h: (h + length_needle)] == needle:  # 则开始判断字符串是否相等
                    return h
        return -1

```
