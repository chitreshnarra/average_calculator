num=0
total=0
while True :
    sval=input('enter a number:')
    if sval == 'done':
        break
    try :
        ival=float(sval)
        num=num+1
        total=total+ival
        print(num,total)
    except:
        print('invalid input')
        continue

print(num,total,total/num)
