
x = int(input("What's x? "))

if x % 2 == 0:
    print("x is even")
else:
    print ("x is odd")

def main():
    x = int(input("What is x? "))
    if is_even(x):     
        print ("x is Even")
    else:
        print ("x is Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
      
main()

# 2 more efficient versions of is_even(n)

def is_even2(n):
    return True if n % 2 == 0 else False

def is_even3(n):
    return (n % 2 == 0) #ie, this will be True if n is even and false if n is odd, giving us the same return value as code above
