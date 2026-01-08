string = input()

resultant_string = ""

for index in range(len(string) - 1):
    resultant_string += string[index] + "-"

resultant_string += string[len(string) - 1]
print(resultant_string)