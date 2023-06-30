from tabulate import tabulate,SEPARATING_LINE
print('Current 1RMs:')
#inputs for initial weights
sq=input('Squat:')
be=input('Bench:')
dl=input('Deadlift:')
ohp=input('OHP:')
#lists of training weights
SQw1=[float(sq)*.65,float(sq)*.75,float(sq)*.85]
SQw2=[float(sq)*.7,float(sq)*.8,float(sq)*.9]
SQw3=[float(sq)*.75,float(sq)*.85,float(sq)*.95]

DLw1=[float(dl)*.65,float(dl)*.75,float(dl)*.85]
DLw2=[float(dl)*.7,float(dl)*.8,float(dl)*.9]
DLw3=[float(dl)*.75,float(dl)*.85,float(dl)*.95]

BEw1=[float(be)*.65,float(be)*.75,float(be)*.85]
BEw2=[float(be)*.7,float(be)*.8,float(be)*.9]
BEw3=[float(be)*.75,float(be)*.85,float(be)*.95]

OHw1=[float(ohp)*.65,float(ohp)*.75,float(ohp)*.85]
OHw2=[float(ohp)*.7,float(ohp)*.8,float(ohp)*.9]
OHw3=[float(ohp)*.75,float(ohp)*.85,float(ohp)*.95]
#table output of training
train=[[' ','Tuesday','Friday'],
       ['Week 1','OHP:'+str(OHw1),'Bench:'+str(BEw1)],
       ['3x5+','Squat:'+str(SQw1),'Deadlift:'+str(DLw1)],
       SEPARATING_LINE,
       ['Week 2','OHP:'+str(OHw2),'Bench:'+str(BEw2)],
       ['3x3+','Squat:'+str(SQw2),'Deadlift:'+str(DLw2)],
       SEPARATING_LINE,
       ['Week 3','OHP:'+str(OHw3),'Bench:'+str(BEw3)],
       ['1x5, 1x3, 1x1+','Squat:'+str(SQw3),'Deadlift:'+str(DLw3)],
       SEPARATING_LINE]

print(tabulate(train, headers='firstrow',tablefmt='simple'))
