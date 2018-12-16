# conversor fahrenheit a celsius
import sys

fahr = float(sys.argv[1])
cel = (5*(fahr-32))/9
print "fahr=", round(fahr,2), "-> cel=", round(cel,2)

