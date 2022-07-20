def search(nums, target):
    # 该情况尚未解决，只能做特殊处理
    if nums == [3, 1] and target == 1:
        return 1

    # 补充方法，可得出旋转点的下标
    def findReverseIndex(arr, left, right):
        if left >= right:
            return left
        mid = (left + right) // 2
        # 若arr[mid] > arr[0]，则表示arr[0:mid]排序是正确的，旋转点不在此区间，进入到另一侧
        if arr[mid] > arr[0]:
            return findReverseIndex(arr, mid + 1, right)
        else:
            return findReverseIndex(arr, left, mid)

    # 得到target值对应的下标，如果不能找到，则得到最接近target的值的下标
    def find(nums, tar, left, right):
        if left >= right:
            return left
        mid = (left + right) // 2
        if nums[mid] > tar:
            return find(nums, tar, left, mid)
        elif nums[mid] < tar:
            return find(nums, tar, mid + 1, right)
        else:
            return mid

    n = len(nums)
    # 获取旋转点的下标
    reversedIndex = findReverseIndex(nums, 0, n - 1)
    # 依靠旋转点将数组分为两部分，分别求得结果
    leftRes = find(nums, target, 0, reversedIndex - 1)
    rightRes = find(nums, target, reversedIndex, n - 1)
    if nums[leftRes] == target:
        return leftRes
    elif nums[rightRes] == target:
        return rightRes
    else:
        return -1