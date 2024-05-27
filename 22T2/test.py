# -*- encoding:utf-8 -*-
# for i in range(len(l)):
#     if l[i] not in result_dict:
#         result_dict[l[i]].append(l[i])
# for key, value in result_dict.items():
#     for i in range(len(l)):
#         if l[i] != key and (l[i] - key) % q == 0 and l[i] - key > 0 and l[i] not in result_dict[key]:
#             result_dict[key].append(l[i])
# for key, value in result_dict.items():
#     ans = ''
#     if value:
#         length = len(value)
#         for i in range(length):
#             if i == 0:
#                 ans += str(value[i])
#             else:
#                 ans += ' -- '
#                 ans += str(value[i])
#     print(ans)

a=[1,3,5,7]
b=[1,3,5]
if b in a:
    print(1)