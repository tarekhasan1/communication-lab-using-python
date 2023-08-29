import math

f = float(input('Enter the frequency in MHz: '))


d = float(input('Enter the distance in Km: " '))
gt = float(input('Enter the tansmitting antenna gain in dB : '))
gr = float(input('Enter the receiving antenna gain in dB : '))
pt = float(input('Enter the tansmitted power in dB : '))

fsl = 32.44+ 20*math.log(d,10) + 20*math.log(f,10)
print('The path loss is :','{:.2f}'.format(fsl),'dB')

pr = pt+gt+gr-fsl
print('The received power is :','{:.2f}'.format(pr),'dB')

prw = math.pow(10,(pr/10))
print('The received power is : ',prw,'watts')