#
# https://adventofcode.com/2022/day/20
#

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

A = []
with open('input.txt') as input:
    for line in input:
        A.append(Node(int(line)))
head = A[0]
node = head
N = len(A)
for i in range(N):
    A[i].prev = A[i - 1]
    A[i].next = A[(i + 1) % N]

for i in range(N):
    node = A[i]
    if not A[i].val:
        continue
    for _ in range(abs(A[i].val)):
        if 0 < A[i].val: node = node.next
        if A[i].val < 0: node = node.prev
    remove = A[i]
    remove.prev.next = remove.next
    remove.next.prev = remove.prev
    insert = remove
    if 0 < A[i].val:
        temp = node.next
        node.next = insert
        insert.next = temp; temp.prev = insert
        insert.prev = node
    if A[i].val < 0:
        temp = node.prev
        node.prev = insert
        insert.prev = temp; temp.next = insert
        insert.next = node

node = A[0]
while node.val:
    node = node.next

t = 0
for k in range(3000 + 1):
    if k == 1000 or k == 2000 or k == 3000:
        t += node.val
    node = node.next
print(f'part 1: {t}')
