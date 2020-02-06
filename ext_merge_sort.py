
def external_sort(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        external_sort(nums, heap_size, largest)


def external_sort_helper(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        external_sort(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        external_sort(nums, i, 0)


def helper():
    res = []
    for i in range(1, 11):
        filePath = f'input/unsorted_{i}.txt'
        file = open(filePath, 'r')
        if file.mode == 'r':
            for i in file.readlines():
                res.append(int(i.strip()))
        external_sort_helper(res)
    return res


def solution():
    res = helper()
    file = open('output/sorted.txt', 'w+')
    for i in res:
        file.write(str(i))
        file.write('\n')


if __name__ == '__main__':
    solution()
