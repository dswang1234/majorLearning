top = int(1e9)


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.add = 0


class segmentTree:
    def __init__(self):
        self.rt = Node()

    # 区间内的线段都加上val值，val可以为负数
    @staticmethod
    def update(node, start, end, l, r, val):
        # 判定此区间是否符合更新的区间，即该区间是否在[l,r]之内；若在，则仅对当前的区间进行标记，且不再往下进行
        if l <= start and end <= r:
            # node.val += (end - start + 1) * val
            node.val += val
            node.add += val
            return
        # 若不在区间[l,r]之内，则继续下沉，直到区间缩小到指定区间内
        segmentTree.pushDown(node)
        mid = (start + end) // 2
        # segmentTree.pushDown(node, mid - start + 1, end - mid)
        if l <= mid:
            segmentTree.update(node.left, start, mid, l, r, val)
        if r > mid:
            segmentTree.update(node.right, mid + 1, end, l, r, val)
        segmentTree.pushUp(node)

    @staticmethod
    # 在区间[l,r]之内查询是否结果
    def query(node, start, end, l, r):
        if l <= start and end <= r:
            return node.val
        segmentTree.pushDown(node)
        mid = (start + end) // 2
        res = 0
        # segmentTree.pushDown(node, mid - start + 1, end - mid)
        if l <= mid:
            res = segmentTree.query(node.left, start, mid, l, r)
        if r > mid:
            res = max(res, segmentTree.query(node.right, mid + 1, end, l, r))
        return res

    @staticmethod
    def pushUp(node):
        # node.val = node.left.val + node.right.val
        node.val = max(node.left.val, node.right.val)

    @staticmethod
    # def pushDown(node, ln, rn):
    def pushDown(node):
        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()
        # node.left.val += node.add * ln
        # node.right.val += node.add * rn
        node.left.val += node.add
        node.right.val += node.add
        node.left.add += node.add
        node.right.add += node.add
        node.add = 0


class MyCalendarTwo:

    def __init__(self):
        self.rt = segmentTree().rt

    def book(self, start: int, end: int) -> bool:
        if segmentTree.query(self.rt, 0, top, start, end - 1) < 2:
            segmentTree.update(self.rt, 0, top, start, end - 1, 1)
            return True
        return False


m = MyCalendarTwo()
print(m.book(10, 20))
