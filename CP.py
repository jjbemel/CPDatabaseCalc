import sympy as sp
from scipy.integrate import quad

files = open("/cpdatabase.prn","r")
x = files.readlines()
files.close()

Compound = []
A = []
B = []
C = []
D = []
for line in x:
    p = line.split("\t")
    Compound.append(p[0])
    A.append(p[1])
    B.append(p[2])
    C.append(p[3])
    D.append(p[4])

row = int(input("Pick a chemical in the database and type the row: "))
T1 = float(input("Type an initial temperature (K): "))
T2 = float(input("Type a final temperature (K): "))

Com2= Compound[row-1]
A2 = A[row-1]
B2 = B[row-1]
C2 = C[row-1]
D2 = D[row-1]

def f(T):
    return float(A[row-1]) + float(B[row-1]) * T + float(C[row-1]) * T**2 + float(D[row-1]) * T**3

i, err = quad(f,T1,T2)

print("\n"+Compound[row-1])
print("-----------")
print("Cp = "+ A2+" + "+B2+"*T + "+C2+"*T^2 + "+D2+"*T^3")
print("\n")
print("Delta H = " + str(i) + " J/mol")
print("With an error of " + str(err))

print("\n")
def f(T):
    return (float(A[row-1]) + float(B[row-1]) * T + float(C[row-1]) * T**2 + float(D[row-1]) * T**3)/T
i, err = quad(f,T1,T2)
print("Delta S = " + str(i) + " J/(K*mol)")
print("With an error of " + str(err))
