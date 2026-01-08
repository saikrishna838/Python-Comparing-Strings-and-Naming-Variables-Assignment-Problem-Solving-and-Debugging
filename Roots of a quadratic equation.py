a=int(input())
b=int(input())
c=int(input())

result_1=(-b+(b**2-4*a*c)**0.5)/(2*a)
result_2=(-b-(b**2-4*a*c)**0.5)/(2*a)

print(round(result_1,2))
print(round(result_2,2))