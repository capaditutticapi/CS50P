mathexpression = input("Expression: ")
mathexpressions = mathexpression.split(" ")

x = float(mathexpressions[0])
z = float(mathexpressions[2])

y = mathexpressions[1]

if y == "+":
    print (x + z)
elif y == "-":
    print (x - z)
elif y == "*":
    print (x * z)
elif y == "/":
    print (x / z)
