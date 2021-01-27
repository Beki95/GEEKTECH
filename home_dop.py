n = input()
n2 = input()
new_n = [int(i) for i in n]
new_n2 = [int(i) for i in n2]
a3, a2, a1 = new_n[0]*100, new_n[1]*10, new_n[2]
b2, b1 = new_n2[0]*10, new_n2[1]
result = a3+a2+a1+b2+b1
print(result)

