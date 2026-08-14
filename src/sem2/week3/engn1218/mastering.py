voltages = [58, 29, 145, 174, 87]

resistors = [4, 5, 15, 20, 22.5]

powers = [voltages[x] ** 2 / resistors[x] for x in range(len(voltages))]
# print(powers)
# print(sum(powers))
VT = 80
R1 = 1500
R2 = 5000
R3 = 3000
R4 = 500
I2 = 12e-3
V2 = R2 * I2
I1 = (VT - V2) / R1
I3 = I1 - I2
V3 = V2 - (I3 * R3)
I4 = (V3 - 0) / R4
IR = I4 - I3
R = (V3 - VT) / IR
print(R)
print("EOL")
