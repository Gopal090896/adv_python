# This is program to claculate simple interest

def simple_interest(p, n, r):
    """This function calculate interest and amount"""
    i = (p*n*r)/100
    a = p+i
    return i, a

# Take p,n,r as input user
p = float(input("please enter pricipile in INR :"))
n = float(input("please enter number in Year :"))
r = float(input("please enter Rate of interest in %p.a. :"))

# call simple interest function
i,a = simple_interest(p,n,r)

#Show the final result
print(f"Simple Intrest : {i:.2f} INR")
print(f"Amount : {a:.2f} INR")
