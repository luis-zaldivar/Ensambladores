lista = ['aaa', 'aad', 'aam', 'aas', 'adc', 'add', 'and', 'call', 'cbw', 'clc', 'cld', 'cli', 'cmc', 'cmp', 'cmpsb', 'cmpsw', 'cwd', 'daa', 'das', 'dec', 'div', 'hlt', 'idiv', 'imul', 'in', 'inc', 'int', 'into', 'iret', 'ja', 'jae', 'jb', 'jbe', 'jc', 'jcxz', 'je', 'jg', 'jge', 'jl', 'jle', 'jmp', 'jna', 'jnae', 'jnb', 'jnbe', 'jnc', 'jne', 'jng', 'jnge', 'jnl', 'jnle', 'jno', 'jnp', 'jns', 'jnz', 'jo', 'jp', 'jpe', 'jpo', 'js', 'jz', 'lahf', 'lds', 'lea', 'les', 'lodsb', 'lodsw', 'loop', 'loope', 'loopne', 'loopnz', 'loopz', 'mov', 'movsb', 'movsw', 'mul', 'neg', 'nop', 'not', 'or', 'out', 'pop', 'popa', 'popf', 'push', 'pusha', 'pushf', 'rcl', 'rcr', 'ret', 'rep', 'repe', 'repne', 'repnz', 'repz', 'ret', 'retf', 'rol', 'ror', 'sahf', 'sal', 'sar', 'sbb', 'scasb', 'scasw', 'shl', 'shr', 'stc', 'std', 'sti', 'stosb', 'stosw', 'sub', 'test', 'xchg', 'xlatb', 'xor']
err=[]

archivoError=open("sintax.err",'w')
asm=open("calculadora.asm",'r')

for l in asm.readlines():
    existe=False
    for i in range(len(lista)):
        l.find(lista[i])
        if l.find(lista[i])!=1:
            existe=True
    if existe==False:
        err.append(l)
if len(err)!=0:
    archivoError.write(err)
archivoError.close()
