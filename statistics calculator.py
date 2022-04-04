import math


# x = []
# xtotal = xf
# f = None
# ftotal = len(x)
# xbar = None
# sd = None
# xbar = x/f
count= 0
Fcount = 0
Xeach = [] #preferably xEach
Feach = []
num_of_entries = int(input('Enter the number of entries in the question: '))
while count != num_of_entries:
    a = float(input('Enter values for X: '))
    Xeach.append(a)
    count += 1

while Fcount != num_of_entries:
    b = float(input('Enter frequency values for X: '))
    Feach.append(b)
    Fcount += 1
    
print('X Values:')
for a in Xeach:
    print(a, end = ' ')
print('')

print('Frequency:')
for a in Feach:
    print(a, end = ' ')
print('')

C = []
for a, b in zip(Xeach, Feach):
    C.append(a*b)

#print(C)
Xtotal = sum(C, 0)
#print(Xtotal)
Ftotal = sum(Feach, 0)
Xbar = Xtotal/Ftotal
print('Mean = ', Xbar)

D = []
for a, b in zip(Xeach, Feach):
    D.append(a*a*b)

#print(sum(D, 0))
sdpt1 = sum(D, 0)/Ftotal
#print(sdpt1)
variance = sdpt1 - (Xbar*Xbar)
print('Variance = ', variance)
sd = math.sqrt(sdpt1 - (Xbar*Xbar))
print('Standard deviation = ', sd)

input('Press enter to exit')