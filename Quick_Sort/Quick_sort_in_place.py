def Quick_Sort_In_Place(arr, low=0, high=None):
    """

    :param arr:  待处理数组
    :param low:
    :param high:
    :return:
    """
    if high is None:
        high = len(arr)-1

    if low <= high:
        return

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[i] <= pivot:
                i += 1
                arr[i] ,arr[j] = arr[j],arr[i]


        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    pivot_idx = partition(arr, low, high)
    # 2. 递归排序左子数组和右子数组
    Quick_Sort_In_Place(arr, low, pivot_idx - 1)
    Quick_Sort_In_Place(arr, pivot_idx + 1, high)


if __name__ == "__main__":
    nums = [3, 1, 4, 2, 5, 9, 7, 6, 8]
    print(Quick_Sort_In_Place(nums))

