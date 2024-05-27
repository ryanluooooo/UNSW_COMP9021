def T32023CPURestore2(lst):
    # positive gap 1. value 需不需要排序 2. value是否重复
    """
    T32023CPURestore2([1, 2, 0, 3, 4])
    gap = 1
        1 - 2
        3 - 4
    gap = 3
        0 - 3
    T32023CPURestore3([0, -10, 20])
    gap = 30
        -10 - 20
    """
    result = {}
    for i in range(len(lst) - 1):
        gap = lst[i + 1] - lst[i]
        if gap < 0:
            continue
        previous_result = result.get(gap, [])
        if [lst[i], lst[i + 1]] not in previous_result:
            previous_result.append([lst[i], lst[i + 1]])
        result[gap] = previous_result

    for key in sorted(result):
        print(f"gap = {key}")
        for line in sorted(result[key]):
            print(f"    {line[0]} - {line[1]}")

T32023CPURestore2([3, 4, 0, 1, 2, 1, 2, 1, 2])