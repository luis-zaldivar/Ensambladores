archivo=open("calculadora.asm", 'r')#abre el archivo en formato de lectura
nuevo=open("cal.lst", 'w')#abre un archivo en formato de escritura
lista = ['aaa', 'aad', 'aam', 'aas', 'adc', 'add', 'and', 'call', 'cbw', 'clc', 'cld', 'cli', 'cmc', 'cmp', 'cmpsb', 'cmpsw', 'cwd', 'daa', 
'das', 'dec', 'div', 'hlt', 'idiv', 'imul', 'in', 'inc', 'int', 'into', 'iret', 'ja', 'jae', 'jb', 'jbe', 'jc', 'jcxz', 'je', 'jg', 'jge', 
'jl', 'jle', 'jmp', 'jna', 'jnae', 'jnb', 'jnbe', 'jnc', 'jne', 'jng', 'jnge', 'jnl', 'jnle', 'jno', 'jnp', 'jns', 'jnz', 'jo', 'jp', 'jpe',
 'jpo', 'js', 'jz', 'lahf', 'lds', 'lea', 'les', 'lodsb', 'lodsw', 'loop', 'loope', 'loopne', 'loopnz', 'loopz', 'mov', 'movsb', 'movsw', 
 'mul', 'neg', 'nop', 'not', 'or', 'out', 'pop', 'popa', 'popf', 'push', 'pusha', 'pushf', 'rcl', 'rcr', 'ret', 'rep', 'repe', 'repne', 
 'repnz', 'repz', 'ret', 'retf', 'rol', 'ror', 'sahf', 'sal', 'sar', 'sbb', 'scasb', 'scasw', 'shl', 'shr', 'stc', 'std', 'sti', 'stosb', 
 'stosw', 'sub', 'test', 'xchg', 'xlatb', 'xor']#arreglo de neumonicos 
def conversion(decimal):#funcion para cobertir decimal a binario
    binario=''
    aux=""
    while decimal>0:
        binario+=str(decimal%2)
        decimal=int(decimal/2)
    binario=binario[::-1]
    if len (binario)<22:
        for i in range(len(binario),8):
            aux+="0"
        binario=aux+binario
    return binario
def omitir(codigo):
    codigo = codigo.split(';')#convierte la linea en un arreglo en la primera posicion lo que esta antes del asterisco y en la segunda lo que esta despues del ;
    codigo = codigo[0]#toma lo que esta en la primera posicon 
    codigo = codigo.replace(' ', '')#remplaza el espacio con nada
    codigo = codigo.replace('\t', '')#remplasa la tabulacion con nada
    codigo = codigo.replace('\n','')
    return True if codigo == '' else False#retorna true si no hay nada en la linea si no regresa false 
def crear():
    cont=0#contador
    for linea in archivo.readlines():#le las lineas de archivo asm
        if omitir(linea):continue
        if linea == '\n': continue
        linea=linea.split(';')#divide en un arreglo la linea en la primera lo que esta antes de la coma y en la siguiente posicion lo que esta despues del ;
        linea=linea[0]#toma la primera posicion 
        linea=linea.replace('\n','')#cambia el salto de linea con nada
        nuevo.write(f"{format(cont, '04d')} {linea}\n")#escribe dentro del archivo lts 
        cont=cont+1#incrementa el contador
    archivo.close()
    nuevo.close()
def etiqueta(l):
    return True if l.count(':') > 0 and  not "\"" in l else False
def obtener_etiqueta(l):
    l = l.split(':')#divide en dos donde se encuentra los dos puntos
    l = l[0]#en la pocicon 0 esta todo lo que esta nates del punto
    l = l.split(' ')#ivide en 2 los espacios para separar la posicion y la etiqueta 
    n = l[0]#gurada la posicion
    l = l[1]#guarda la etiqueta
    n = n.replace('\t', '')#queita la tabulacion posiciones 
    n = n.replace(' ', '')#quita los espacios posiciones
    l = l.replace('\t', '')#quita las tabulacones para la etiqueta 
    l = l.replace(' ', '')#quita el espacio para las etiquetas 
    return n, l
def etiquetas():
    archivo=open("cal.lst",'r')#abrimos
    p,e=[],[]#arreglo de posicion y etiquetas 
    con=-1
    for li in archivo:#recorremos el archivo
        con+=1#incrementamos el contador 
        if not etiqueta(li):continue#verifa que exista una etiqueta 
        n,l=obtener_etiqueta(li)#guardamos la poscion y la etiqueta 
        p.append(n)#llenamos las posiciones se crearn las etiquetas
        e.append(l)#llenamos las etiquetas
    archivo.close()#cerramos el archivo
    contenido=[]#arreglo para guardar el contenido nuevo
    for j in open("cal.lst",'r'):
        if not '\"' in l and j.count(':') == 0:
            num=[str(n)for n,p in zip (p,e)if p in j]#recorre el archivo y pone la posicion donde se usa la etiqueta
            if (num !=[]):#vemos si el arreglo tiene algo 
                j=j.replace('\n','')#quitamos el salto de linea 
                j+=' '+str(num)+'*****************\n'#sobrescribimos la linea donde se usa la etiqueta 
        contenido.append(j)#guardamos la sobrescritura
    nue=open("cal.lst",'w')#abrimos el archivo en formato de escritura
    nue.writelines(contenido)#escribimos en el archivo 
    nue.close()#se cierra el archivo
def neumonicos():
    code=False#para verificar el segmentio de codigo
    fin=False#para saber cuando finalice 
    pos=[]#arreglo donde se guardan posicion
    neu=[]#lista de neumonicos
    error=open("erroresxD.err",'w')#creamos un archivo para guardar los erroes
    with open("cal.lst")as archivo:#abrimos el archivo lst
        for j in archivo:#recorremos el archivo 
            j=j.split(' ')#dividimos los espacios
            n=j[0]#guradmaos la posicion
            j=j[1]#gurdamos el neumonico
            if ".code"in j:code=True#verifica que ya paso el segmento code
            if code and not fin:#verifica que este en el segmento de codigo 
                if '.model' in j or 'stack' in j or '.data' in j or 'end' in j: fin = True
                else:
                    if not '.code' in j:#
                        if ':'in j:continue #si existe dos punto lo ignora 
                        j=j.replace('\t','')#quita la tabulacion
                        j=j.replace('\n','')#quita el salto de linea 
                        j=j.replace(' ','')#quita los espacios
                        pos.append(n)#guradamos las posiciones de los neumonicos
                        neu.append(j)#gurdamos los neumonicos
    for i in range(len(neu)):#recorremos la lista de neumonicos
        if neu[i]in lista:continue#verificamos que el neumonico este en la lista 
        else:
            error.write(f"Sintax Error {pos[i]} {neu[i]}\n")#si no esta el neumonico escribe en el archivo err 
    archivo=open("cal.lst",'r')#abrimos el archivo lst
    file=archivo.readlines()#guardamos el contenido del archivo en una variable 
    fin=file[len(file)-1]#obtenenmos el final de la lista 
    fin =fin.split(' ')#dividimos por espacios la linea de texto 
    fin=fin[1]#nos quedamos con la parte del texto
    fin=fin.replace('\n','')#quitamos el salto de liena
    if fin!='end':#verificamos que lo que este el final es diferente a end
        error.write("no contiene end") #si li es escribimos un mensaje de error que se guardara en el archivo err
    error.close()#cerramos el archivo de los errores

crear()
etiquetas()
neumonicos()