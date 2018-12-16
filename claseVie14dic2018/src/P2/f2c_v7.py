# conversor fahrenheit a celsius 

fahr = 0.0
while fahr < 101: 
	cel = (5*(fahr-32))/9
	print "fahr=", round(fahr,2), "-> cel=", round(cel,2)
	fahr = fahr + 10
