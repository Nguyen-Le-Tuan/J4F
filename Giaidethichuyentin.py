#Đảo ngược chuỗi nguyên lí:
""" string = str(input())
string2 = ""
n = len(string) 
for i in range(1, (n+1)):
    string2 = string2 + str(string[n-i])
print(string2) """

#Giải
a = str(input("Input a: "))
n = len(a)
k = int(input("Input k: "))
list1 = list(reversed(a))
print(list1)
for i in range(n):
    list1 = ''.join(list1.append((list[i])**k))
print(list1)
