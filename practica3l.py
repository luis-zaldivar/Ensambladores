Archasm = open('calculadora.asm' , 'r') #lee el archivo asm
Archlst = open('etiquetas.lst' , 'w') #escribe en el docuemnto lst
lista = ['aaa', 'aad', 'aam', 'aas', 'adc', 'add', 'and', 'call', 'cbw', 'clc', 'cld', 'cli', 'cmc', 'cmp', 'cmpsb', 'cmpsw', 'cwd', 'daa', 
'das', 'dec', 'div', 'hlt', 'idiv', 'imul', 'in', 'inc', 'int', 'into', 'iret', 'ja', 'jae', 'jb', 'jbe', 'jc', 'jcxz', 'je', 'jg', 'jge', 
'jl', 'jle', 'jmp', 'jna', 'jnae', 'jnb', 'jnbe', 'jnc', 'jne', 'jng', 'jnge', 'jnl', 'jnle', 'jno', 'jnp', 'jns', 'jnz', 'jo', 'jp', 'jpe',
 'jpo', 'js', 'jz', 'lahf', 'lds', 'lea', 'les', 'lodsb', 'lodsw', 'loop', 'loope', 'loopne', 'loopnz', 'loopz', 'mov', 'movsb', 'movsw', 
 'mul', 'neg', 'nop', 'not', 'or', 'out', 'pop', 'popa', 'popf', 'push', 'pusha', 'pushf', 'rcl', 'rcr', 'ret', 'rep', 'repe', 'repne', 
 'repnz', 'repz', 'ret', 'retf', 'rol', 'ror', 'sahf', 'sal', 'sar', 'sbb', 'scasb', 'scasw', 'shl', 'shr', 'stc', 'std', 'sti', 'stosb', 
 'stosw', 'sub', 'test', 'xchg', 'xlatb', 'xor']


conta = 0 # contador inicialiado en cero

for line in Archasm: #recorre el archivo asm por linea
    elim = True 

    #busca espacios en blanco, saltos de linea y tabulaciones.
    for carac in line: 
        if carac  != '\n' and carac != '\t' and carac != ' ':
            elim = False
#eliminacion de comentarios en el archivo asm
    C = line.split(';')
    C = C[0]
    C=C.replace('\n','')

    if elim is False and not C == "" and not C =='\n' :
        Archlst.write(format(conta, '04d'))#agrega al archivo lts numero decimal con 4 digitos
        Archlst.write(" ")
        Archlst.write(C)
        Archlst.write("\n")
        conta +=1
Archasm.close()#cierra el archivo asm
Archlst.close()#cierra el archivo lts
#numerar etiquetas
Archetiq = open('etiquetas.lst','r')#abrir archivo generado con los renglones enumerados
listas = [[],[]] #guardar etiquetas

#recorre el archivo etiquetas.lst
for line in Archetiq:
    if ':' in line and not "\"" in line:
        line = line.split(':')#identifica las etiquetas
        line = line[0] #toma el primer lugar de la linea
        line = line.split(' ')#el split se utiliza para dividir en esta caso si se encuentra un espacio
        numero = line[0] #posicion cero de la listas (numero de renglon)
        line = line[1]#posicion uno (etiqueta)
        line = line.replace('\t', ' ')#eliminatabulacion
        listas[0].append(numero)#agrega el numero del renglon en el ssubindice cero
        listas[1].append(line)#agrega la etiqueta en el subindice uno
Archetiq.close() #cierra el archivo

Archetiq = open('etiquetas.lst','r') #lee el archivo generado 

listLis = [] #guarda el numero de la linea segun la etiqueta
for line in Archetiq:#recorrer cada linea del archivo
    if not ':' in line and not '\"' in line: #condicion para realizar lo que se pide si se encuentra una etiqueta
        i=0 #inicializa en cero
        numero=0
        
        while(i<len(listas[0])): #tamaño de lista a abrir
            if (listas[1][i]in line):
                numero = listas[0][i]
                print(listas[1][i]) #muestra las etiquetas existentes
                break
        
            i += 1
        if(numero != 0):
            line = line.replace('\n', '')#eliminar dalto de linea
            line += '      ==>' + numero + '\n'#el numero equivalente a la etiqueta lo muestra
    listLis.append(line)

Archetiq = open('etiquetas.lst','w') #escribe en el documento
Archetiq.writelines(listLis)#exscribe en las lineas la equivalencia
Archetiq.close()#cierra el archivo

segmento=False# verificar el segmentio de codigo
final=False#para saber cuando finalice 
posicion=[]#arreglo donde se guardan posicion
instruc=[]#lista de neumonicos

error=open("errores.err",'w')#creamos un archivo para guardar los erroes
with open("etiquetas.lst")as Archetiq:#abrimos el archivo lst

        for line in Archetiq:#recorremos el archivo 
            line=line.split(' ')#divide los espacios
            n=line[0]#guardala posicion
            line=line[1]#guarda mnemonico

            if ".code"in line:segmento=True#verifica que ya paso el segmento code
            if segmento and not final:#verifica que este en el segmento de codigo 
                if '.model' in line or 'stack' in line or '.data' in line or 'end' in line: fin = True
                else:
                    if not '.code' in line:#
                        if ':'in line:continue 
                        line=line.replace('\t','')
                        line=line.replace('\n','')
                        line=line.replace(' ','')
                        posicion.append(n)
                        instruc.append(line)#gurdamos los neumonicos
print(instruc)
for i in range(len(instruc)):#recorremos la lista de neumonicos
        if instruc[i]in lista:continue#verificamos que el neumonico este en la lista 
        else:
           error.write(f"Sintax Error {posicion[i]} {instruc[i]}\n")#si no esta el neumonico escribe en el archivo err 
Archetiq=open("etiquetas.lst",'r')#abrimos el archivo lst
file=Archetiq.readlines()#guardamos el contenido del archivo en una variable 
final=file[len(file)-1]#obtenenmos el final de la lista 
final =final.split(' ')#dividimos por espacios la linea de texto 
final=final[1]#nos quedamos con la parte del texto
final=final.replace('\n','')#quitamos el salto de liena

error.close()
 