# -*- coding：utf-8 -*-
# &Author  AnFany

# 5_Longest_Palindromic_Substring 最长回文子串


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 利用动态规划的方法
        # d[i-1,j-1]表示从索引i-1到索引j-1构成的回文子串
        # 因此对于如果s[i]=s[j]，则d[i,j]也是回文子串

        length = len(s)
        # 当s的长度不大于1时
        if length <= 1:
            return s

        # 因为获取新的回文子串时，前后都加了元素，也就是长度增加了2，因此分2种情况，
        # 一是从长度为1的回文子串开始
        # 二是从长度为2的回文子串开始

        # 获取起始的回文子串长度为2的，然后再依次增加长度
        # 长度为2的回文子串，就是连续的2个字母是一样的
        # 存储每一次回文子串的列表，不用存储字符串，只存储索引即可
        start_2_list = [[0, 0]]  # 因为start_2_list可能为空集，编程便利性
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                start_2_list.append([i, i+1])
        # 存储目前为止最长的回文子串的索引
        longest_index_2 = start_2_list[-1]
        while start_2_list:
            new_2_list = []
            for k in start_2_list:
                start, end = k[0] - 1, k[1] + 1
                if start >= 0 and end < length:
                    if s[start] == s[end]:
                        new_2_list.append([start, end])

            start_2_list = new_2_list
            if start_2_list:
                longest_index_2 = start_2_list[-1]

        # 获取起始长度为1的回文子串，然后再依次增加长度
        # 长度为1的回文子串，字符串中所有的都是
        # 存储每一次回文子串的列表，不用存储字符串，只存储索引即可
        start_1_list = [[g, g] for g in range(length)]

        # 存储目前为止最长的回文子串的索引
        longest_index_1 = start_1_list[-1]
        while start_1_list:
            new_1_list = []
            for k in start_1_list:
                start, end = k[0] - 1, k[1] + 1
                if start >= 0 and end < length:
                    if s[start] == s[end]:
                        new_1_list.append([start, end])
            start_1_list = new_1_list
            if start_1_list:
                longest_index_1 = start_1_list[-1]

        #  获取两种情况回文子串最长的
        len_1 = longest_index_1[1] - longest_index_1[0]
        len_2 = longest_index_2[1] - longest_index_2[0]

        if len_1 > len_2:
            return s[longest_index_1[0]: longest_index_1[1] + 1]
        else:
            return s[longest_index_2[0]: longest_index_2[1] + 1]





