f = open('all2.txt','r')
res = open('all3.txt','w')
how = 1
pharmacy = []
howcomms = 0
for i in f:
    if how%2==0:
        if i.strip() not in pharmacy:
            url = i.strip()
            res.write(f'\n{url}')
    else:
        try:
            comms = i.strip().replace(',','\n')
            res.write(f'{comms}')
        except:
            name = i.strip()
            res.write(f'{name}')
    how+=1
f.close()
res.close()