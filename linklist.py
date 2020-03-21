"""
linklist.py
功能： 实现单链表的构建和功能操作
重点代码
"""
"""
头部节点不能丢，一般用p来操作，头部节点不变。
"""
import time


# 创建节点类
class Node:
    """
    思路：将自定义的类视为节点的生成类，实例对象中
        包含数据部分和指向下一个节点的next
    """

    def __init__(self, value, next=None):
        self.next = next  # 循环下一个节点关系
        self.value = value  # 有用数据


# node1 = Node(1)
# node2 = Node(2, node1)  # node2.next=node1
# node3 = Node(3, node2)  # node3.next=node2

# 做链表操作
class LinkList:
    """
    思路：单链表类，生成对象后可以进行增删改查操作
        具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化列表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        # for i in list_:
        #     self.next = (i, self.next)  这是自己写的，好像不对。
        p = self.head  # p作为移动变量
        for i in list_:
            p.next = Node(i)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.value)
            p = p.next  # p向后移动

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, value):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)

    # 头部插入（一定要先把头部的连接送给新节点，才能让新节点连接下面的）
    def head_insert(self, value):
        node = Node(value)  # 第一步：生成节点
        node.next = self.head.next  # 第二步：新节点连接下一个节点（通过head.next）
        self.head.next = node  # 第三步：将头节点与新生成节点连接

    # 指定插入位置
    def insert(self, index, value):
        p = self.head
        i = 0
        while i < index:
            """防止index超出位置最大范围"""
            if p.next is None:
                break
            i = i + 1
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node

    # # 删除节点（自己写的）
    # def del_(self, index):
    #     p = self.head
    #     i = 0
    #     p1 = p
    #     while i <= index:
    #         """防止index超出位置最大范围"""
    #         if p.next is None:
    #             break
    #         i = i + 1
    #         p1 = p
    #         p = p.next
    #     p1.next = p.next
    #     p.next = None
    # 删除节点
    def remove(self, value):
        p = self.head
        # 结束循环必然两个条件其一为假.
        # 先判断是否为None为好，以防p.next已经是None而没有value值报错。
        # and只要有一个不行，后面的就不执行。所以有判断顺序
        while p.next and p.next.value != value:
            p = p.next
        if p.next is None:
            raise ValueError("value not in list")
        else:
            p.next = p.next.next

    # # 获取某节点的值（自己写的）
    # def get_value(self, index):
    #     p = self.head
    #     i = 0
    #     while p.next and i <= index:
    #         i += 1
    #         p = p.next
    #     if p.next is None:
    #         raise IndexError("list index out of range")
    #     else:
    #         return p.value
    # 获取某节点的值
    def get_value(self, index):
        p = self.head.next
        i = 0
        for i in range(index):
            if p.next is None:
                raise IndexError("list index out of range")
            p = p.next
        return p.value


# l=[1,2,3,4,5]
# link = LinkList()
# link.init_list(l)
# link.get_value(888)

"""
模块被调用时会先被执行一次
"""
# l=list(range(6))
# for i in l:
#     print(i)
# print(type(l))


# l = LinkList()
# l.head.next = Node(1)
# print(l.next.value)
# l = LinkList()
# l.init_list([1, 2, 3, 4, 5])
# l.show()
# l = [1, 2, 3]
# l1 = [1, 2, 3, 4]
# print(id(l))
# print(id(l1))
# print(id(l[1]))
# print(id(l1[1]))
# 列表遍历时间
l = list(range(10000))
tm = time.time()
for i in l:
    print(i)
a = time.time() - tm
# 链表遍历时间
l1 = LinkList()
l1.init_list(l)
tm = time.time()
l1.show()
b = time.time() - tm
print("遍历列表运行时间：", a)
print("遍历链表运行时间：", b)
