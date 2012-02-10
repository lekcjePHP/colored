import os
import sys

if os.getuid() == 0:
	print ("jestes rootem")
else:
	print("sorry nie jestes rootem")	
	sys.exit()#natychmiasowe wylacznei programu

