# this a script to decode ROT coded texts
#BY:abdellah lamine a.k.a (dystopian)

#your encripted text goes here.
encripted="Axeeh Ftg Ahp Tkx Rhn Whbgz"

#start of our program
for i in range (1,26):
	decripted=""
	for j in encripted:

		if j==" ": 
				decripted+=" "
				continue
		#check lower cases
		if j.islower():
		
			#check if we exceded the bound of ascci alphabits
			if ord(j)+i>ord("z"):
				#if yes we first have to know with how much we excceded over the 26 alphabit
				decripted+=chr(((ord(j)+i)-97)%26+97)
			else:
				decripted+=chr(ord(j)+i)
		#check upper cases
		elif j.isupper():

			 if ord(j)+i>ord("Z"):
				
				decripted+=chr(((ord(j)+i)-65)%26+65)
			else:
				decripted+=chr(ord(j)+i)

	print('i=',i ,":",decripted)