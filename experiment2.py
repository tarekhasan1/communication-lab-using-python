import math

pt = float(input('Enter the input power in watts :'))
Gt = float(input('Enter the transmitting antenna gain in db : '))
Gr = float(input('Enter the receiving antenna gain in db : '))
d = float(input('Enter the distance in Km :'))
f = float(input('Enter the frequency in MHz :'))
rfl = float(input('Enter the receiver feeder loss in db : '))
aa = float(input('Enter the atmospheric absorption in db :'))
pl = float(input('Enter the polarization loss in db :'))
aml = float(input('Enter the antenna misalignment loss in db :'))

Pt = 10*math.log(pt,10) #calculation transmitted power in dB
EIRP = Pt + Gt #calculating Eirp
fsl = 32.4 + 20*math.log(d,10) + 20*math.log(f,10) #calculating path loss 
losses = fsl + rfl + aa + aml + pl
P = EIRP +Gr - losses

print('Total loss = '+str(losses) +'dB')
print('Total losses power ='+str(P)+'dB')
