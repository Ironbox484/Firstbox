def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError: #can remove ZeroDivisionError
        print("Error: Cannot divide by zero.")
print(int(div42by(2)))
print(div42by(12))
print(div42by(0))
print(div42by(1))
print("Above is a test")
print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")

print("How many kilos do you want to loose?")
kilos=input()
try:
    if int(kilos) < 0:
        print("You actually want to GAIN more weight??!?!?!")
    elif int(kilos) <17:
        print("probbly higher than that right? :D")
    elif int(kilos) >= 25:
        print("Calm down ffs")
    
    else:
        print("that sounds about right")
except:
    print("enter a number bro")
#Githubed?