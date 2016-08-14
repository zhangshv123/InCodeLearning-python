#!/usr/bin/python
#题目：有一个list，里面有n个学生，有一个值d，从index 0开始取第d个学生，把他放到新的list上面，在从新的index开始取第d个学生，放入新的list。。。。6 o) |  M- 
#
#假如有5个学生，分别是1，2，3，4，5，d是4
#第一次 1 2 3 5             4
#第二次 1 2 5              4 3
#第三次 1 2                4 3 5
#第四次 1                4 3 5 2
#第五次                  4 3 5 2 1,
class CNode:
	val = 0
	next
	def __init__(self,v):
		self.val = v
def delete(node, k):
	res = []
	while(node.next!=node):
		for _ in range(k-2):
			node = node.next
		res += node.next.val,
		node.next = node.next.next
		node = node.next
	res += node.val,
	return res

c1 = CNode(1)
c2 = CNode(2)
c3 = CNode(3)
c4 = CNode(4)
c5 = CNode(5)
c1.next = c2
c2.next = c3
c3.next = c4
c4.next = c5
c5.next = c1
print delete(c1, 4)
