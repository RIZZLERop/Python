#Make a calculator on terminal

#Make functions

def add():
    add = num1+num2
    print(add)

def sub():
    sub = num1+num2
    print(sub)

def mult():
    mult = num1+num2
    print(mult)

def div():
    div = num1+num2
    print(div)

def error():
    print("ERROR FOUND -- |INPUT ERROR|")

#Make a loop 

while True:
                                                        #Two numbers input
    num1 = int(input("Number1?"))
    num2 = int(input("Number2?"))
                                                        #Input of opperator 
    Opt = input("Select your operator[+,-,*,/]")
                                                        #If and Else -- conditions
    if Opt == "+":
        add()
    elif Opt == "-":
        sub()
    elif Opt == "*":
        mult()
    elif Opt == "/":
        div()
    else:
        error()