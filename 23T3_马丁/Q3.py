from itertools import product
def T32023CPURestore3(string):
    """
    T32023CPURestore3("12_ + 2_0 = 33_")
    120 + 210 = 330
    T32023CPURestore3("_ + ___ = ___")
    0 + 0 = 0
    """
    # word = string.split("=")
    # result = word[1]
    # number1, number2 = word[0].split("+")

    # 找到所有结果——》 最小值
    # 找到的第一个就已经是最小值
    all_result = []
    count_repeat = string.count("_")
    for possible_answer in product(range(10), repeat=count_repeat):
        possible_word = ""
        count_line = 0
        for char in string:
            if char != "_":
                possible_word += char
            else:
                possible_word += str(possible_answer[count_line])
                count_line += 1

        word = possible_word.split("=")
        result = word[1]
        number1, number2 = word[0].split("+")
        if int(number1) + int(number2) == int(result):
            all_result.append([int(number1), int(number2), int(result)])
    all_result = sorted(all_result, key=lambda x: x[2])

    print(all_result[0])


    # pass

T32023CPURestore3("_ + ___ = ___")
# from itertools import product
# result = product(range(10), repeat=4)
# for line in result:
#     print(line)