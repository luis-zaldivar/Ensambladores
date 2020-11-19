arc=open("cal.lst",'r')
file=arc.readlines()
arc.close()
fin=file[len(file)-1]
fin =fin.split(' ')
fin=fin[1]
fin=fin.replace('\n','')
print(fin)