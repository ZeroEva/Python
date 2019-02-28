#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return self.getNum(num1) * self.getNum(num2)

    def getNum(self, num_str):
        exp = 0
        num = 0
        for char in reversed(num_str):
            num = num + self.str2num(char) * (10 ** exp)
            exp += 1
        return num

    def str2num(self, char):
        if '0' == char:
            return 0
        if '1' == char:
            return 1
        if '2' == char:
            return 2
        if '3' == char:
            return 3
        if '4' == char:
            return 4
        if '5' == char:
            return 5
        if '6' == char:
            return 6
        if '7' == char:
            return 7
        if '8' == char:
            return 8
        if '9' == char:
            return 9


# solution = Solution()
# multiply = solution.multiply("123", "456")
# print(multiply)
num1 = "123"
num2 = "456"
product = [0] * (len(num1) + len(num2))
print(product)
