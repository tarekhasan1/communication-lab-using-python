EIRPu = float(input('Enter the uplink EIRP : '))   #Equivalent isotropic radiated power
EIRPd = float(input('Enter the downlink EIRP : '))

GTRu = float(input('Enter the uplink GTR : '))
GTRd = float(input('Enter the downlink GTR : '))

FSLu = float(input('Enter the uplink FSL : '))    #Free-space loss
FSLd = float(input('Enter the downlink FSL : '))

RFLu = float(input('Enter the uplink RFL : '))      #Received feeder loss
RFLd = float(input('Enter the downlink RFL : '))

AAu = float(input('Enter the uplink AA : '))    #atmospheric absorption
AAd = float(input('Enter the downlink AA : '))

AMLu = float(input('Enter the uplink AML : '))  #antenna misallignment losses
AMLd = float(input('Enter the downlink AML : '))

lossu = FSLu + RFLu + AAu + AMLu
print('Uplink loss', lossu)

lossd = FSLd + RFLd + AAd + AMLd
print('Donwlink loss', lossd)

CNRu = EIRPu + GTRu - lossu + 228.6
print('Total carrier to noise ratio for uplink is ' + str(CNRu) + ' decilog')

CNRd = EIRPd + GTRd - lossd + 228.6
print('Total carrier to noise ratio for downlink is '+ str(CNRd) +' decilog')

CNRt = (CNRu * CNRd)/(CNRu+CNRd)
print('Total carrier to noise ratio is ','{:.2f}'.format(CNRt),'decilog')