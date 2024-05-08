# Take Principal (P) , Period (N) Years, Rate of Intrest (R) %p.a.and 
P = float(input('Please enter Principal in INR : '))
N = float(input('Please enter Period in Years :'))
R = float(input('please enter rate of Intrest in %.p.a. :'))

#Calculate simple intrest
I = (P*N*R)/100

# Calculate Amount
A = P + I

#print above results
print(f'Simple Intrest for given values is {I :.2f} INR')
print(f'Amount is  {A : .2f} INR')
