'''lista = ['aaa', 'aad', 'aam', 'aas', 'adc', 'add', 'and', 'call', 'cbw', 'clc', 'cld', 'cli', 'cmc', 'cmp', 'cmpsb', 'cmpsw', 'cwd', 'daa', 
'das', 'dec', 'div', 'hlt', 'idiv', 'imul', 'in', 'inc', 'int', 'into', 'iret', 'ja', 'jae', 'jb', 'jbe', 'jc', 'jcxz', 'je', 'jg', 'jge', 
'jl', 'jle', 'jmp', 'jna', 'jnae', 'jnb', 'jnbe', 'jnc', 'jne', 'jng', 'jnge', 'jnl', 'jnle', 'jno', 'jnp', 'jns', 'jnz', 'jo', 'jp', 'jpe',
 'jpo', 'js', 'jz', 'lahf', 'lds', 'lea', 'les', 'lodsb', 'lodsw', 'loop', 'loope', 'loopne', 'loopnz', 'loopz', 'mov', 'movsb', 'movsw', 
 'mul', 'neg', 'nop', 'not', 'or', 'out', 'pop', 'popa', 'popf', 'push', 'pusha', 'pushf', 'rcl', 'rcr', 'ret', 'rep', 'repe', 'repne', 
 'repnz', 'repz', 'ret', 'retf', 'rol', 'ror', 'sahf', 'sal', 'sar', 'sbb', 'scasb', 'scasw', 'shl', 'shr', 'stc', 'std', 'sti', 'stosb', 
 'stosw', 'sub', 'test', 'xchg', 'xlatb', 'xor']
err=[]
ints=[[],[]]
    
def comparar():
    code=False
    fin=False
    error=open("errores.err",'w')
    with open("cal.lst")as archivo:
        for j in archivo:
            j=j.split(' ')
            n=j[0]
            j=j[1]
            
            if ".code"in j:code=True
            
            if code and not fin:
                if '.model' in j or 'stack' in j or '.data' in j or 'end' in j: fin = True
                else:
                    if not '.code' in j:
                        if ':'in j:continue 
                        j=j.replace('\t','')
                        j=j.replace('\n','')
                        j=j.replace(' ','')
                        ints[0].append(n)
                        ints[1].append(j)
    pos=ints[0]
    neu=ints[1]
    for i in range(len(neu)):
        if neu[i]in lista:continue
        else:
            error.write(f"Sintax Error {pos[i]} {neu[i]}\n")
    archivo=open("cal.lst",'r')
    file=archivo.readlines()
    fin=file[len(file)-1]
    fin =fin.split(' ')
    fin=fin[1]
    fin=fin.replace('\n','')    
    if fin!='end':
        error.write("no contiene end")  
    error.close()     
comparar()
'''
datos=[]
parametros=[]
def segData():
    archivo=open("cal.lst",'r')
    data=False
    fin=False
    for i in archivo:
        i=i.split(" ")
        n=i[0]
        i=i[1]
        if ".data"in i:data=True
        if data and not fin:
            if '.model' in i or 'stack' in i or '.code' in i or 'end' in i: fin = True
            else:
                if not '.data' in i:
                    i=i.replace('\n','')
                    i=i.replace('\t','')
                    datos.append(i)
    archivo.close()
def para():
    
    code=False
    fin=False
    error=open("errores.err",'w')
    with open("cal.lst")as archivo:
        for j in archivo:
            
            if ".code"in j:code=True
            
            if code and not fin:
                if '.model' in j or 'stack' in j or '.data' in j or 'end' in j: fin = True
                else:
                    if not '.code' in j:
                        j=j.split(" ")
                        print(j)

print("jaja")
segData()
para()