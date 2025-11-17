# Ask the user for : Principal(P), Rate(R), Time(T).
# Convert all to float and compute simple interest

Principal = input("Enter Principal amount : ")
Rate = input("Enter rate : ")
Time = input("Enter Time : ")

P = float(Principal)
R = float(Rate)
T = float(Time)

SI = (P*R*T)/100
print("Simple Intrest = ", SI)
