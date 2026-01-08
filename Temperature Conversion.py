temperature = input()
unit=temperature[-1]
value=temperature[:-1]
if (unit=="C" or unit=="c"):
    Celsiu=float(value)
    print(str(round(Celsiu,2))+"C")
    print(str(round((Celsiu*9/5)+32,2))+"F")
    print(str(round(Celsiu+273,2))+"K")
elif (unit=="F" or unit=="f"):
    fahrenheit=float(value)
    print(str(round((fahrenheit-32)*5/9,2))+"C")
    print(str(round(fahrenheit,2))+"F")
    print(str(round((fahrenheit-32)*5/9+273,2))+"K")
elif(unit=="k" or unit=="K"):
    kelivn=float(value)
    print(str(round(kelivn-273,2))+"C")
    print(str(round((kelivn-273)*9/5+32,2))+"F")
    print(str(round(kelivn,2))+"K")