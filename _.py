# WIN = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
# d = {1: "0", 9: "x", 2: "0", 3: "0", 4: '0', 5: "0", 6: "1",  7: "0"}
# # print(d.keys())
# # print(d.values())
# # print(d.items())
# for w, x in zip(WIN, d):
#     try:
#         if d[w[0]] == d[w[1]] == d[w[2]]:
#             print(w, x)
#     except:
#         pass

dict_ = {1:"sd", 2:2}
print(dict_)
for i in dict_.items():
    dict_[i[0]] = " n"

print(dict_)