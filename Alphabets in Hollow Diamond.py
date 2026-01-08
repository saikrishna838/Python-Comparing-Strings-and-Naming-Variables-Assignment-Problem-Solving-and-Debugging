n = int(input())

for i in range(2*n-1):
    if i==0 or i==2*n-2:
        left_space=(" ")*(n-1)
        row=left_space+chr(65)
        print(row)
    elif i<n:
        left_space=(" ")*(n-i-1)
        hollow_space=(" ")*(2*i-1)
        row=left_space+chr(64+(i*2))+hollow_space+chr(65+2*i)
        print(row)
    else:
        left_space=(" ")*(i-n+1)
        hollow_space=(" ")*((2*n-1) - (2*(i-n+2)))
        row= left_space+chr(64+((2*n-i-2)*2))+hollow_space+chr(65+(2*n-i-2)*2)
        print(row)