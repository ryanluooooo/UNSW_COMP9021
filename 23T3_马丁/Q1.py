from pprint import pprint
def T32023CPURestore1(lst):
    """
    >>> T32023CPURestore1([4, 4, 3])
    * *
    * * *
    * * *
    * * *
    >>> T32023CPURestore1([0, 1, 2, 3, 2, 1, 0])
         *
       * * * 
     * * * * *
    """
    result = []
    for i in range(max(lst)):
        result.append([])

    for num in lst:
        append_star_count = 0
        for i in range(len(result)):
            if append_star_count < num:
                result[i].append("*")
                append_star_count += 1
            else:
                result[i].append(" ")
    
    for line in result[::-1]:
        print(" ".join(line))

    # result = [[] for i in range(max(lst))]
    # print(result)

T32023CPURestore1([4, 4, 3])