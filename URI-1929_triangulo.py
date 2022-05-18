varetas = input().split()

vareta1 = int(varetas[0])
vareta2 = int(varetas[1])
vareta3 = int(varetas[2])
vareta4 = int(varetas[3])

if vareta1 + vareta2 > vareta3 and vareta2 + vareta3 > vareta1 and vareta1 + vareta3 > vareta2:
    print('S')
elif vareta2 + vareta3 > vareta4 and vareta3 + vareta4 > vareta2 and vareta2 + vareta4 > vareta3:
    print('S')
elif vareta1 + vareta3 > vareta4 and vareta3 + vareta4 > vareta1 and vareta1 + vareta4 > vareta3:
    print('S')
elif vareta1 + vareta2 > vareta4 and vareta2 + vareta4 > vareta1 and vareta1 + vareta4 > vareta2:
    print('S')
else:
    print('N')