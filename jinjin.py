# input
total_number = int(input())
input_list = []
for i in range(total_number):
    a, b = map(int, input().split())
    input_list.append(a+b)

# input_list = [8, 8, 9, 8, 9, 4, 6]
max_i = 0
for i in input_list:
    if i > 8 and i > max_i:
        max_i = i

if max_i == 0:
    print(0)
else:
    print(input_list.index(max_i)+1)
