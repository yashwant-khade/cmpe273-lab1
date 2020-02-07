import asyncio
from concurrent.futures import ThreadPoolExecutor


def external_sort(arr, size, index):
    largest = index
    left_child = (2 * index) + 1
    right_child = (2 * index) + 2

    if left_child < size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        external_sort(arr, size, largest)


def external_sort_helper(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        external_sort(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        external_sort(arr, i, 0)


async def helper(THREAD_POOL):
    loop = asyncio.get_event_loop()
    coroutines = []
    for i in range(1, 11):
        file_path = 'input/unsorted_{0}.txt'.format(i)
        coroutine = loop.run_in_executor(THREAD_POOL, solution, file_path)
        coroutines.append(coroutine)
    await asyncio.gather(*coroutines)


def solution(file_path):
    coroutines = []
    file = open(file_path, 'r')
    if file.mode == 'r':
        for j in file.readlines():
            ds.append(int(j.strip()))
    return coroutines


THREAD_POOL = ThreadPoolExecutor(4)


if __name__ == '__main__':
    import time
    start = time.time()
    ds = []
    loop = asyncio.get_event_loop()
    loop.run_until_complete(helper(THREAD_POOL))
    external_sort_helper(ds)
    file = open('output/async_sorted.txt', 'w')
    for i in ds:
        file.write(str(i))
        file.write('\n')
    end = time.time()
    file = open('output/async_time.txt', 'w')
    file.writelines(str(end - start))
