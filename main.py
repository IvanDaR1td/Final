#2652035
# Ask for name
name = input("What is your name?")
print("Hey",name.capitalize(),", let's Go...")
#input x
x = float(input("Please input a real number x such that - 0.5 < x < 0.5 "))
if x < 0.5 or x > -0.5:
    print("Thank you.")
#Define f(x)
    def f(x):
        root1 = 1+x+x**2+x**3+x**4+x**5+x**6+x**7+x**8+x**9+x**10
        return(root1)
#Define g(x)
    def g(x):
        import math
        a = math.log(2,math.e)
        if x > 0:
            root2 = 2*a
        elif x < 0:
            root2 =-2*a
        elif x == 0:
            root2 = 0
        return(root2)
#Define h(x)
    def h(x):
        root3 = 1/(1-x)
        return(root3)
# average of the three results
    def avg(x):
        root4 = (f(x)+g(x)+h(x)/3)
        return(root4)
#print f(x),g(x),h(x) and average
    print("The value of f",(x),"is",f(x))
    print("The value of g",(x),"is",g(x))
    print("The value of h",(x),"is",h(x))
    print("The average of te three results above is",avg(x))

#quit
print("Goodbye:)")
quit()