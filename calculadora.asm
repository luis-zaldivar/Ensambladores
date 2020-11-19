.model small ;modelo del programa 
.stack
.data
	m db 10,10,13," M E N U ",10,13,"1. Suma ",10,13,"2. Resta ",10,13,"3. Multiplicacion ",10,13,"4. Division ",10,13,"5. Salir $"
	mop db 10,"Ingrese la opcion deseada: $" ;mensaje al usuario
	op db 0 ;variable para seleccionar opciones
	ms db 10,10,"Gracias, hasta pronto $" ; Mensaje de salida
	me db 10,13,"Opcion Invalida ",10,13,36 
	mi db 10,13,"Ingrese numero: $" ;Mensaje para solicitar datos
	n1 db 0 ;variable para el primer numero 
	n2 db 0 ; variable para el segundo numero
	pot db 10 ; potencia para recibir dos datos 
	m1 db 10,10,13,"S U M A ",10,13,36 ; mensajes al usuario
	m2 db 10,10,13,"R E S T A ",10,13,36
	m3 db 10,10,13,"M U L T I P L I C A C I O N",10,13,36
	m4 db 10,10,13,"D I V I S I O N ",10,13,36
	m5 db 10, 13,"Resultado: $"
	runidades db 0 ;guarda las unidades del resultado
	rdecenas db 0 ;guarda las decenas del resultado 
.code
	mov ax, @data ; mueve los datos al codigo 
	mov ds, ax ;libera ax guardando en ds
 
	mov ah, 00h ;instruccion para limpiar la pantalla
	mov al, 03h
	int 10h

	Menu:
		mov ah, 09h ;muestra el menu 
		lea dx, m
		int 21h ; llamada al DOS

		mov ah, 09h ; muestra mensaje para datos
		lea dx, mop
		int 21h

	jmp SelOpcion ; brinta a la rutina de selección

	SelOpcion:
		mov ah, 01h ;solicita la opcion 
		int 21h ; llamada al DOS
		sub al, 30h ;resta 30h para ajuste ASCII
		mov op, al ; copia el valor a op

		cmp op,1 ;comparativa opcion 1
		je sumar ;brinca a rutina sumar

		cmp op,2 ; comparativa opcion 2
		je restar ; brinca a rutina restar

		cmx op,3 ;comparativa opcion 3
		je multi ; brinca a rutina multi

		cmp op,4 ;comparativa opcion 4
		je divide ; brinca a rutina divide

		cmp op, 5 ; comparativa a salida 
		je salida ;brinca a rutina salida

	OpNoValida:
		mov ah, 09h ; muestra mensaje 
		lea dx, me
		int 21h
		jmp Menu ;regresa a menu 

	sumar:
		call datos ; llama a datos 
		call Suma ; llama a rutina Suma
		jmp Menu ; brinca a menu

	restar:
		call datos ;llama a datos 
		call Resta ; llama a Resta
		jmp Menu ; brinca a Menu

	multi:
		call datos ;llama a datos 
		call Multiplicacion ; llama a multiplicacion
		jmp Menu ; brinca a menu 
	divide:
		call datos ; llama a datos 
		call Division ; llama a division 
		jmp Menu ; brinca al menu 
	
	salida:
		coll Salir ; llama a rutina

	datos:
		mov ah, 09h ; muestra mensaje 
		lea dx, mi
		int 21h ;llamada al DOS 
		mov ah, 01h ; pide dato 
		int 21h
		sub al, 30h ;Ajuste ASCII
		mul pot ;hace decena el primer dato
		mov n1,al ; copia el resultado de mul
		mov ah, 01h ; solicita dato
		int 21h ;llamada al DOS
		sub al, 30h ;Ajuste ASCII
		add n1, al ;suma las decenas + unidades 

		mov ah, 09h ;Solicita el segundo numero
		lea dx, mi
		int 21h
		mov ah, 01h
		int 21h
		sub al, 30h
		mul pot
		mov n2,al
		mov ah, 01h
		int 21h
		sub al, 30h
		add n2, al
		ret ; retorna
	
	Suma:
		mov ah, 09h ;muestra mensaje 
		lea dx, m1
		int 21h

		xor ax,ax ; limpia el registro
		mov al, n1 ;copia nq al registro
		add al, n2 ; suma: al=al+n2
		aam ; Ajuste ASCII
		or ax,3030h 
		mov runidades,al ;parte baja 
		mov rdecenas, ah ; parte alta

		mov ah, 09h ; muestra mensaje 
		lea dx, m5
		int 21h

		mov ah, 02h ;muestra decenas 
		mov dl, rdecenas
		int 21h

		mov ah, 02h ; muestra unidades 
		mov dl, runidades
		int 21h		
		ret

	Resta:
		mov ah, 09h ; muestra mensaje 
		lea dx, m2
		int 21h

		xor ax,ax ; limpia registro AX
		mov al, n1 ; copia n1 en al 
		sub al, n2 ; resta: al=al-n2
		aam ; ajuste ASCII
		or ax,3030h
		mov runidades,al ; parte baja
		mov rdecenas, ah ; parte alta 

		mov ah, 09h ; muestra mensaje 
		lea dx, m5
		int 21h

		mov ah, 02h ; muestra decenas 
		mov dl, rdecenas
		int 21h

		mov ah, 02h ; muestra unidades 
		mov dl, runidades
		int 21h
		ret ; retorno

	Multiplicacion:
		mov ah, 09h ; muestra mensaje 
		lea dx, m3
		int 21h

		xor ax,ax ; limpia registro
		mov al, n1 ; guarda n1 en al
		mul n2 ; multiplica: al=al*n2
		aam ; ajuste ASCII
		or ax, 3030h 
		mov rdecenas, ah ; parte alta 
		mov runidades, al ; parte baja

		mov ah, 09h ; muestra mensaje 
		lea dx, m5 ; 
		int 21h

		mov ah, 02h ;muestra decenas 
		mov dl, rdecenas
		int 21h

		mov ah, 02h ; muestra unidades 
		mov dl, runidades
		int 21h
		ret ;retorno

	Division:
		mov ah, 09h ; muestra mensaje 
		lea dx, m4 
		int 21h

		xor ax,ax ; limpua registro AX
		mov al, n1 ; copia en al valor n1
		div n2 ;division: al=al/n2
		aam ;Ajuste ASCII
		or ax, 3030h
		mov rdecenas, ah ; parte alta
		mov runidades, al ; parte baja

		mov ah, 09h ;muestra mensaje 
		lea dx, m5 
		int 21h

		mov ah, 02h
		mov dl, rdecenas ;impime las decenas 
		int 21h

		mov ah, 02h ; imprime unidades
		mov dl, runidades
		int 21h
		ret

	Salir:
		mov ah, 09h ;muestra mensaje de salida 
		lea dx, ms
		int 21h

		mov ah, 4ch ;termina programa
		int 21h ;devuelve control al DOS