import sys

# conversor fahrenheit a celsius 
if len(sys.argv) != 2:
	print "uso: f2c valor\n"
else:
	fahr = float(sys.argv[1])
	cel = (5*(fahr-32))/9
	print "fahr=", round(fahr,2), "-> cel=", round(cel,2)
	

