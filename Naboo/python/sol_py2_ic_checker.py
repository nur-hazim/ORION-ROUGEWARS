ic=str(input('Enter the IC to be validated: '))

a=int(ic[1])
b=int(ic[2])
c=int(ic[3])
d=int(ic[4])
e=int(ic[5])
f=int(ic[6])
g=int(ic[7])

total= a*2 + b*7 + c*6 + d*5 + e*4 + f*3 + g*2 + 4
remainder = total%11

last = ic[8]

validity = (last=='J' and remainder==0) or\
           (last=='Z' and remainder==1) or\
           (last=='I' and remainder==2) or\
           (last=='H' and remainder==3) or\
           (last=='G' and remainder==4) or\
           (last=='F' and remainder==5) or\
           (last=='E' and remainder==6) or\
           (last=='D' and remainder==7) or\
           (last=='C' and remainder==8) or\
           (last=='B' and remainder==9) or\
           (last=='A' and remainder==10)


print('Validity of the IC:',validity)
