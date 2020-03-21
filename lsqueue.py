"""
lqueue.py：队列的链式存储
重点代码

思路分析：
1.源于链表构建队列模型
2.用链表的开头作为队头，链表结尾位置作为队尾。
3.单独定义队尾标记，避免每次插入数据遍历
4.队头和队尾重叠，队列为空。
"""


# 自定义异常
class QueueError(Exception):
    pass


# 定义节点类
class Node:

    def __init__(self, value, next=None):
        self.next = next
        self.value = value


# 队列操作
# class LSqueue:
#     def __init__(self):
#         # 标记栈的栈顶位置
#         self._top = Node(None)
#         self._end = self._top
#
#     def is_empty(self):
#         return self._top is self._end
#
#     def enqueue(self, value):
#         self._end.next = Node(value)
#         self._end = self._end.next
#
#     def dequeue(self):
#         self._top = self._top.next
#         if self._top is None:
#             raise QueueError("Stack is empty")
#         else:
#             value = self._top.value
#             return value
"""----------------------------------"""


class LSqueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self._head=self._top = self._end = Node(None)

    def is_empty(self):
        return self._end == self._top

    # 入队，尾动。end动
    def enqueue(self, value):
        # self._end = Node(value, next=self._end)是错误的，这是end往前移动而不是后移
        self._end.next = Node(value)
        self._end = self._end.next

    # 出队，头动
    def dequeue(self):
        if self._top == self._end:
            raise QueueError("Stack is empty")
        self._top = self._top.next
        # print(self._head.next.value)这一串代码说明指针走而链表没变
        return self._top.value
    # def check_fuhao(self):
    #     if self._top in ["(","[","}",")","]","}"]:
    #         self


if __name__ == "__main__":
    print("----------")
    ls = LSqueue()  # 初始化栈
    ls.enqueue(10)
    ls.enqueue(20)
    ls.enqueue(30)
    # a=ls.dequeue()
    # print(a)
    while not ls.is_empty():
        print(ls.dequeue())
