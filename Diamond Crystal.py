n = int(input())

for i in range(1, n + 1):
    spaces1 = n - i
    spaces2 = 2 *(i - 1)
    row = " " * spaces1 + "/" + " " * spaces2 + "\\"
    print(row)
for j in range(1, n + 1):
    spaces1 = j - 1
    spaces2 = 2 * (n - j)
    row = " " * spaces1 + "\\" + " " * spaces2 + "/"
    print(row)