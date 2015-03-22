n=input('write the number n for th matrix')
print "This game 2 players will input according to their theycan fill either 'x' or '0'"
print "When it is written you won tha last user who gave input wins"
def List(n):
		L1=[]
		for i in range (0,n):
			x=range(i*n+1,(i+1)*n+1)
			L1= L1+[x]
		return L1
def checkposition(x,L):
	a=x/n
	b=x%n
	if b==0:
		return L[a-1][n-1]
	else:
		return L[a][b-1]
def checkinput(k,x,L):
	if x>(n**2):
		print 'give correct input1'
		return 1
	elif (type(x) is int)==False:
		print 'give correct input2'
		return 1
	elif checkposition(x,L)=='x' or checkposition(x,L)=='0':
		print 'give correct input3'
		return 1
	elif (k!='x' and k!='0'):
		print 'give correct input4'
		return 1
def update(x,k,L):
	a=x/n
	b=x%n
	if b==0:
		L[a-1][n-1]=k
		return L
	else:
		L[a][b-1]=k
		return L
def g(n):
	x=str(n*2)
	return len(x)
def Map(n,L):
	Map=L
	for i in range(0,2*n):
		if i%2==0:
        		for j in range(0,2*n):
				if j%2==0:
					x=str(Map[i/2][j/2])
        				print x.center(g(n)+1),
        			else:
        		        	print "|",
		else:
			print ''
	return ''
import sys
def compare(i,k,L):
	c=L
	for j in range (0,n):
		if c[i][j]==k:
			continue
		else:
			return -1
	return 1
def compare1(j,k,L):
	c=L
	for i in range (0,n):
		if c[i][j]==k:
			continue
		else:
			return -1
	return 1
def compare4(a,k):
	for i in range (0,n):
		if compare(i,k,a)==1:
			return 1
		else:
                        continue
	return -1
def compare5(a,k):
	for j in range (0,n):
		if compare1(j,k,a)==1:
			return 1
		else:
                        continue
	return -1
def compare2(k,L):
	c=L
	for i in range (0,n):
		if c[i][i]==k:
			continue
		else:
			return -1
	return 1
def compare3(k,L):
	c=L
	for i in range (0,n):
		if c[i][n-1-i]==k:
			continue
		else:
			return -1
	return 1

def allfilled(n,a):
	for i in range (0,n):
		for j in range (0,n):
			if a[i][j]=='x' or a[i][j]=='0':
				continue 
			else:
				return -1
	return 1
def user(n):
	L1=List(n)
	a=L1
	print Map(n,L1)
	for i in range (0,n**3):
		if i%2==0:
			k=input('write the input which you have to fill')
			x=input('write the place where you have to fill')
			if checkinput(k,x,a)==1:
				continue
			else:
				a=update(x,k,L1)
				L1=a
				if compare3(k,a)==1 or compare2(k,a)==1 or compare4(a,k)==1 or compare5(a,k)==1:
					print ' you won'
					print Map(n,a)
					return 1
					sys.exit()
				elif allfilled(n,a)==1:
					print 'game drwan'
					print Map(n,a)
					return 1
				else:
					print Map(n,a)
		else:
			k=input('write the input which you have to fill')
			x=input('write the place where you have to fill')
			if checkinput(k,x,a)==1:
				continue
			else:
				a=update(x,k,L1)
				L1=a
				if compare3(k,a)==1 or compare2(k,a)==1 or compare4(a,k)==1 or compare5(a,k)==1:
					print ' you won'
					print Map(n,a)
					return 1
					sys.exit()
				elif allfilled(n,a)==1:
					print 'game drawn'
					print Map(n,a)
					return 1
				else:
					print Map(n,a)
user(n)
c=2
while c%2==0:
	a=input('do you want to play again 2 for yes and 1 for no')
	if a==1:
            break
        n=input('write the number n for the matrix size')
        print "This game 2 players will input according to their theycan fill either 'x' or '0'"
        print "When it is written you won tha last user who gave input wins"
	user(n)
	c=c+a

	

	

	
