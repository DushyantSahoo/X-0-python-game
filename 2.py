from graphics import *
print 'when the window opens click once to start the game'
n=input('write the value of n*n matrix')
def lis(n):
    L=[]
    a=0
    while a<n:
        L.append([0])
        b=0
        while b<n-1:
            L[a].append(0)
            b=b+1
        a=a+1
    return L

L= lis(n)
win=GraphWin('Tic Tac Toe',1000,600)
a=400/n
b=400/n
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
            if a[i][j]=='X' or a[i][j]=='O':
                continue 
            else:
                return -1
    return 1
def Screen1():
    for i in range (0,n):
        for j in range (0,n):
            if (i+j)%2==0:
                rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                rect.setFill("Red")
                rect.draw(win)
            else:
                rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                rect.setFill("Green")
                rect.draw(win)
    win.getMouse()
def isInside(p,rect):
    rectP1 = rect.getP1()
    rectP2 = rect.getP2()
    if(p.getX() >= rectP1.getX() and p.getX() <= rectP2.getX() and 
       p.getY() >= rectP1.getY() and p.getY() <= rectP2.getY()):
        return True
    else:
             return False

def Pext():
    Screen1()
    i=2
    while i<n**n:
        i=i+(n-1)
        if i%(2*(n-1))==0:
            ctext=Text(Point(550,50),"Try to click to turn by turn")
            ctext.setSize(12)
            ctext.draw(win)
            dtext=Text(Point(670,100),"Incase you click outside or on some box which is already filled click once more")
            dtext.setSize(12)
            dtext.draw(win)
            etext=Text(Point(650,150),"When it is written you won last user who clicked wins")
            etext.setSize(12)
            etext.draw(win)
            itext=Text(Point(200,550),"click where you have to fill your choice")
            itext.setTextColor("Blue")
            itext.setSize(12)
            ftext.Text(Point(650,200),"if you want to exit click on the X at the righttop corner of the screen")
            ftext.setSize(12)
            ftext.draw(win)
            itext.draw(win)
            inputP=win.getMouse()
            if isInside(inputP,Rectangle(Point(0,0),Point(a*n,b*n))):
                for l in range (0,n):
                    for j in range (0,n):
                        rect=Rectangle(Point(j*a,l*b),Point((j+1)*a,(l+1)*b))
                        if isInside(inputP,rect):
                            c=rect.getCenter()
                            if L[l][j]=='O':
                                i=i-(n-1)
                                
                            else:
                                k=Text(c,"X")
                                k.draw(win)
                                L[l][j]='X'
                                k='X'
                                if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                    q=Text(Point(500,300),'You Won')
                                    q.draw(win)
                                    return 1
                                elif allfilled(n,L)==1:
                                     w=Text(Point(500,300),'Game drawn')
                                     w.draw(win)
                                     return 1
                                else:
                                    continue
                                break
                        else:
                            continue
            else:
                for i in range (0,n):
                    for j in range (0,n):
                        rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                        if isInside(inputP,rect):
                            c=rect.getCenter()
                            if L[i][j]=='O':
                                i=i-(n-1)
                                
                            else:
                                k=Text(c,"X")
                                k.draw(win)
                                L[i][j]='X'
                                k='X'
                                if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                    q=Text(Point(500,300),'You Won')
                                    q.draw(win)
                                    return 1
                                elif allfilled(n,L)==1:
                                     w=Text(Point(500,300),'Game drawn')
                                     w.draw(win)
                                     return 1
                                else:
                                    continue
                            break
                        else:
                            continue
        else:
            inputP=win.getMouse();
            itext=Text(Point(200,550),"click where you have to fill your choice")
            itext.setTextColor("Blue")
            itext.setSize(12)
            itext.draw(win)
            if isInside(inputP,Rectangle(Point(0,0),Point(a*n,b*n))):
                for i in range (0,n):
                    for j in range (0,n):
                        rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                        if isInside(inputP,rect):
                            c=rect.getCenter()
                            if L[i][j]=='X':
                                i=i-(n-1)
                                
                            else:
                                k=Text(c,"O")
                                k.draw(win)
                                L[i][j]='O'
                                k='O'
                                if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                    q=Text(Point(500,300),'You Won')
                                    q.draw(win)
                                    return 1
                                elif allfilled(n,L)==1:
                                     w=Text(Point(500,300),'Game drawn')
                                     w.draw(win)
                                     return 1
                                else:
                                    continue
                            break
                        else:
                            continue
            else:
                for i in range (0,n):
                    for j in range (0,n):
                        rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                        if isInside(inputP,rect):
                            c=rect.getCenter()
                            if L[i][j]=='X':
                                i=i-(n-1)
                                
                            else:
                                k=Text(c,"O")
                                k.draw(win)
                                L[i][j]='O'
                                k='O'
                                if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                    q=Text(Point(500,300),'You Won')
                                    q.draw(win)
                                    return 1
                                elif allfilled(n,L)==1:
                                     w=Text(Point(500,300),'Game drawn')
                                     w.draw(win)
                                     return 1
                                else:
                                    continue
                            break
                        else:
                            continue
while Pext()==1:
    f=Text(Point(300,450),'want to play again click on the tic tac toe region and for exit click anywhere else')
    f.draw(win)
    z=win.getMouse()
    if isInside(z,Rectangle(Point(0,0),Point(a*n,b*n))):
        win.close()
        win=GraphWin('Tic Tac Toe',800,600)
        print 'when the window opens click once to start the game'
        n=input('write the value of n*n matrix')
        a=400/n
        b=400/n
        def Screen1():
            for i in range (0,n):
                for j in range (0,n):
                    if (i+j)%2==0:
                        rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                        rect.setFill("Red")
                        rect.draw(win)
                    else:
                        rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                        rect.setFill("Green")
                        rect.draw(win)
            win.getMouse()
        def lis(n):
            L=[]
            a=0
            while a<n:
                L.append([0])
                b=0
                while b<n-1:
                    L[a].append(0)
                    b=b+1
                a=a+1
            return L
        L=lis(n)
        def Pext():
            Screen1()
            i=2
            while i<n**n:
                i=i+(n-1)
                if i%(2*(n-1))==0:
                    ctext=Text(Point(550,50),"Try to click to turn by turn")
                    ctext.setSize(12)
                    ctext.draw(win)
                    dtext=Text(Point(670,100),"Incase you click outside or on some box which is already filled click once more")
                    dtext.setSize(12)
                    dtext.draw(win)
                    etext=Text(Point(650,150),"When it is written you won last user who clicked wins")
                    etext.setSize(12)
                    etext.draw(win)
                    ftext.Text(Point(650,200),"if you want to exit click on the X at the righttop corner of the screen")
                    ftext.setSize(12)
                    ftext.draw(win)
                    itext=Text(Point(200,550),"click where you have to fill your choice")
                    itext.setTextColor("Blue")
                    itext.setSize(12)
                    itext.draw(win)
                    inputP=win.getMouse()
                    if isInside(inputP,Rectangle(Point(0,0),Point(a*n,b*n))):
                        for l in range (0,n):
                            for j in range (0,n):
                                rect=Rectangle(Point(j*a,l*b),Point((j+1)*a,(l+1)*b))
                                if isInside(inputP,rect):
                                    c=rect.getCenter()
                                    if L[l][j]=='O':
                                        i=i-(n-1)
                                        
                                    else:
                                        k=Text(c,"X")
                                        k.draw(win)
                                        L[l][j]='X'
                                        k='X'
                                        if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                            q=Text(Point(500,300),'You Won')
                                            q.draw(win)
                                            return 1
                                        elif allfilled(n,L)==1:
                                             w=Text(Point(500,300),'Game drawn')
                                             w.draw(win)
                                             return 1
                                        else:
                                            continue
                                        break
                                else:
                                    continue
                    else:
                        jtext=Text(Point(200,550),"Please click correctly")
                        jtext.setTextColor("Pink")
                        jtext.setSize(12)
                        jtext.draw(win)
                        for i in range (0,n):
                            for j in range (0,n):
                                rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                                if isInside(inputP,rect):
                                    c=rect.getCenter()
                                    if L[i][j]=='O':
                                        i=i-(n-1)
                                        
                                    else:
                                        k=Text(c,"X")
                                        k.draw(win)
                                        L[i][j]='X'
                                        k='X'
                                        if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                            q=Text(Point(500,300),'You Won')
                                            q.draw(win)
                                            return 1
                                        elif allfilled(n,L)==1:
                                             w=Text(Point(500,300),'Game drawn')
                                             w.draw(win)
                                             return 1
                                        else:
                                            continue
                                    break
                                else:
                                    continue
                else:
                    inputP=win.getMouse();
                    itext=Text(Point(200,550),"click where you have to fill your choice")
                    itext.setTextColor("Blue")
                    itext.setSize(12)
                    itext.draw(win)
                    if isInside(inputP,Rectangle(Point(0,0),Point(a*n,b*n))):
                        for i in range (0,n):
                            for j in range (0,n):
                                rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                                if isInside(inputP,rect):
                                    c=rect.getCenter()
                                    if L[i][j]=='X':
                                        i=i-(n-1)
                                        
                                    else:
                                        k=Text(c,"O")
                                        k.draw(win)
                                        L[i][j]='O'
                                        k='O'
                                        if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                            q=Text(Point(500,300),'You Won')
                                            q.draw(win)
                                            return 1
                                        elif allfilled(n,L)==1:
                                             w=Text(Point(500,300),'Game drawn')
                                             w.draw(win)
                                             return 1
                                        else:
                                            continue
                                    break
                                else:
                                    continue
                    else:
                        jtext=Text(Point(200,550),"Please click correctly")
                        jtext.setTextColor("Pink")
                        jtext.setSize(12)
                        jtext.draw(win)
                        for i in range (0,n):
                            for j in range (0,n):
                                rect=Rectangle(Point(j*a,i*b),Point((j+1)*a,(i+1)*b))
                                if isInside(inputP,rect):
                                    c=rect.getCenter()
                                    if L[i][j]=='X':
                                        i=i-(n-1)
                                        
                                    else:
                                        k=Text(c,"O")
                                        k.draw(win)
                                        L[i][j]='O'
                                        k='O'
                                        if compare3(k,L)==1 or compare2(k,L)==1 or compare4(L,k)==1 or compare5(L,k)==1:
                                            q=Text(Point(500,300),'You Won')
                                            q.draw(win)
                                            return 1
                                        elif allfilled(n,L)==1:
                                             w=Text(Point(500,300),'Game drawn')
                                             w.draw(win)
                                             return 1
                                        else:
                                            continue
                                    break
                                else:
                                    continue
        
    else:
        win.close()

                
            

