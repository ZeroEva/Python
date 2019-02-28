#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        end = head
        flag = False
        while l1 and l2:
            val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            print(flag, val)
            if flag:
                val += 1
                flag = False
            if val >= 10:
                val -= 10
                flag = True

            new_node = ListNode(val)
            end.next = new_node
            end = new_node
        ll = None
        if l1:
            ll = l1
        if l2:
            ll = l2
        while ll or flag:
            if ll:
                val = ll.val
                ll = ll.next
                if flag:
                    val += 1
                    flag = False
                if val >= 10:
                    val -= 10
                    flag = True
            else:
                val = 1
                flag = False

            new_node = ListNode(val)
            end.next = new_node
            end = new_node
        return head.next

    def addTwoNumbers2(self, l1, l2):
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        node = None
        for char in str(num1 + num2):
            new_node = ListNode(char)
            new_node.next = node
            node = new_node
        return node

    def getNum(self, node):
        exp = 0
        num = 0
        while node:
            num = num + node.val * (10 ** exp)
            exp += 1
            node = node.next
        return num


solution = Solution()
ll1 = ListNode(1)
ll2 = ListNode(9)
ll2.next = ListNode(9)
_node = solution.addTwoNumbers2(ll1, ll2)
while _node:
    print(_node.val)
    _node = _node.next
