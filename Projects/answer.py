

#["Amir", 1,2,3]
#["James", 3,4,5]
#
#
#
#

def get_input(n):
    data = []
    for i in range(n):
        input_line = input()
        splitted_input_line = input_line.split()
        splitted_input_line[1] = float(splitted_input_line[1])
        splitted_input_line[2] = float(splitted_input_line[2])
        splitted_input_line[3] = float(splitted_input_line[3])
        data.append(splitted_input_line)


n = int(input())
f = 1
for i in range(1, n+1):
    f = f * i
print(f)