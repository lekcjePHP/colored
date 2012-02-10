import os
import sys

COMMAND_NOT_FOUND_ERROR_CODE = 32512


if os.getuid() == 0:
	print ("OK")
	
else:
	print("sorry nie jestes rootem")	
	sys.exit()#natychmiasowe wylacznei programu

print("Za chwile bedziemy aktualizowac system..")
if os.system('yaourt') == COMMAND_NOT_FOUND_ERROR_CODE:
	os.system("pacman -Syu")
else: 
	os.system('yaourt -Syu')