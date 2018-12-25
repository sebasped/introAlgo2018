def producto(n, m):
	if m == 0:
		return 0
	else:
		return n + producto(n, m-1)

print producto(2,2)
print producto(3,4)
print producto(6,10) 