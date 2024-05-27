def T32023CPURestore4(row, col, start="A"):
    """
    >>> T32023CPURestore4(4, 4)
    AHIP
    BGJO
    CFKN
    DELM
    >>> T32023CPURestore4(4, 4, start="B")
    BIJQ
    CHKP
    DGLO
    EFMN
    """
    lines = [""] * row
    
    rule = []
    for i in range(row):
        rule.append(i)
    rule = rule + rule[::-1]
    char = start

    # print(rule)
    # gap = ord(start) - ord("A")
    # [0, 1, 2, 3, 3, 2, 1, 0]
    # gap = 2 i = 25 27
    for i in range(row * col):
        # char = chr(ord("A") + ((i + gap) % 26))
        line_index = rule[i % len(rule)]
        lines[line_index] = lines[line_index] + char
        if char == "Z":
            char = "A"
        else:
            char = chr(ord(char) + 1)
        # 0 0
        # 1 1
        # 4 3
        # 5 2
        # 15 % 8 = 7 0



        # 0 % 8  0 0
        # 1 1
        # 2 2

        # 4 % 8 = 4    3 -1
        # 5 % 8 = 5    2 -2
        # 6 1 -3
        # if i % (2 * row) < row:
        #     lines[i % (2 * row)] = lines[i % (2 * row)] + char
        # else:
        #     row_index = 2 * row - i % (2 * row) - 1
        #     lines[row_index] = lines[row_index] + char
        # lines[i % row] = lines[i % row] + char
    for line in lines:
        print(line)

T32023CPURestore4(4, 4, "X")
