def f(x):
	return {
		'a': 1,
		'b': 2,
	}[x]
	
def manad(x):
	return {
		1: 'Januari',
		2: 'Februari',
		3: 'Mars',
		4: 'April',
		5: 'Maj',
		6: 'Juni',
		7: 'Juli',
		8: 'Augusti',
		9: 'September',
		10: 'Oktober',
		11: 'November',
		12: 'December',
	}[x]
	
print(f('b'))
print(manad(4))