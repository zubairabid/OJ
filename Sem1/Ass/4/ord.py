#diff arr for all 3
#check sign change
#if any, 


def gret( a, b ):
	return (a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2]) and not( a[0] == b[0] and a[1] == b[1] and a[2] == b[2] )
for _ in range(input()):
	a = map( int, raw_input().split() )
	b = map( int, raw_input().split() )
	c = map( int, raw_input().split() )
	if not ( gret( a, b ) or gret (b,a) ):
		print "no"
		continue
	if not ( ( a[0]>=b[0] and ( (gret( a, c ) and gret( c,b)) or gret(b,c) or gret(c,a) ) ) or (a[0] <= b[0] and ( gret( c,b) or gret( a,c) or (gret(c,a) and gret(b,c))))):
		print "no"
		continue
	print "yes"


