import math

#initialisation of variables

ncore=float(input('Enter the ncore : '))
nclad= float(input('Enter the ncald : '))

NA =math.sqrt(ncore**2-nclad**2)

#Results
print('The numerical aperture = ',round(NA,5))
