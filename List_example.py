import datetime
AllPatients = 'p'
UrgentPatients = 'u'
SoVrski = 'v'
now = datetime.datetime.now()
now = now.hour
name = str(input('Hi gorgeous, what is your name?'))
p = ['Mile', 'Pero', 'Milena', 'Jovanka', 'Dragica', 'Limonka', 'Chedomir', 'Meri', 'Dragoljub']
u = p [1:4]
v = p [4]

if(now < 12):
    print('Good morning,' + name)
elif (now >=12 and now <=18):
    print('Good day,' + name)
else:
    print ('Good evening,' + name)
    
print ('Do you want to see your list of patients?')
Answer = str(input('For YES, type y:'))
if Answer == "y":
    typeoflist = str(input('For the full list of patients, type p. For Urgent patients type u. For  VIP patients, type v:'))

if Answer != "y":
    print('Ok, I assume you are not interested in the patient list. Have a great day, then!')

if typeoflist == 'p':
    print (p)
    print ('You have ' + str(len(p)) + ' patients in total for today.')
elif typeoflist == 'u':
    print (u)
    print ('You have ' + str(len(u)) + ' urgent patients in total for today.')
elif typeoflist == 'v':
    print (v) 
    print ('You have ' + str(len(v)) + ' VIP patients in total for today.')
else:
    print ('We do not have such list of patients.')
    
# add ValueError 
print: ('I assume you are not interested in the patient list. Have a great day, Doc!')

# after each choice of a list: p, u or v print the list lenght, i.e. total number of patients. Currently, the program shows total number of patients only for the first chosen list.
# fix the error after if Answer != "y": print('I assume you are not interested in the patient list.'). 
    


