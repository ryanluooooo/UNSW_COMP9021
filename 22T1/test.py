total_nb_of_letters=100
letter_list = []
for i in range(total_nb_of_letters):
    x = 65 + i
    if x > 90:
        x -= 26
    letter_list.append(chr(x))
print(letter_list)