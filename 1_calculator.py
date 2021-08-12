#Create a two input calculator (Mathematical,Bitwise, Relational,):
##Function Define:
#Mathematical operation:
def sum(a,b):
    c=a+b
    print('Addition of Two no.',a,'+',b,'=',c)
def sub(a,b):
    c=a-b
    print('substraction of Two No. ',a,'-',b,'=',c)
def mul(a,b):
    c=a*b
    print('Multiplication of Two No.',a,'x',b,'=',c)
def div(a,b):
    c=a/b
    d=a//b
    e=a%b
    print('Division of Two No. ',a,'/',b,'=',c)
    print('Floor division of Two No. ',a,'//',b,'=',d)
    print('Mod of Two No. ',a,'%',b,'=',e)
def pow(a,b):
    c=a**b
    print('Power calculation',a,'^',b,'=',c)

#Bitwis Operation:
def bitand(a,b):
    c= a & b
    print(a,'&',b,'=',c)
def bitor(a,b):
    c= a | b
    print(a,'|',b,'=',c)
def bitnot(a):
    c=~a
    print('~',a,'=',c)
def bitxor(a,b):
    c= a ^ b
    print(a,'^',b,'=',c)
def bitshiftleft(a, c):
    m= a >> c
    print(a, "shifted left by ", c, "=", m)
def bitshiftright(a, c):
    n= a << c
    print(a, "shifted right by", c, "=", n)

#Relational Operation:
def rela(a,b):
    if(a>b):
        print(a,'>',b)
    elif(a<b):
        print(a,'<',b)
    elif(a==b):
        print(a,'=',b)
    elif(a>=b):
        print(a,'>=',b)
    elif(a<=b):
        print(a,'<=',b)
    else:
        print(a,'not equal to',b)
#invalid choice:
def wrong():
    print('Syntax Error')
def inv():
    print('Invalid Choice')
##############################
##User input part:
print('\n This is a Multiple Calculator')
option=input('\n For Mathematical  Operation Press M\n '
      'For Bitwise Operation Press B '
      '\n For Relational Operation Press R\n:')
#Mathematical Part:
if(option=='M'):
    print('MODE: Mathematical\n')
    a=float(input('Enter the First No. :'))
    b=float(input('Enter the second No. :'))
    op=input('\nChoose your Operation + , - , * , D , P :')
    if(op=='+'):
        sum(a,b)
    elif(op=='-'):
        sub(a,b)
    elif(op=='*'):
            mul(a,b)
    elif(op=='D'):
            div(a,b)
    elif(op=='P'):
            pow(a,b)
    else:
        wrong()
#Bitwis Part:
elif(option=='B'):
    print('MODE: Bitwise')
    op=input('\nChoose your operation &, |, ~, ^, for left_shift:l, for right_shift:r  ::')
    if(op=='&'):
        a=int(input('Enter First No.:'))
        b=int(input('Enter Second No.:'))
        bitand(a,b)
    elif(op=='|'):
        a = int(input('Enter First No.:'))
        b = int(input('Enter Second No.:'))
        bitor(a, b)
    elif(op=='~'):
            a = int(input('Enter The No.:'))
            bitnot(a)
    elif(op=='^'):
            a = int(input('Enter First No.:'))
            b = int(input('Enter Second No.:'))
            bitxor(a, b)
    elif(op=='l'):
            a = int(input('Enter The No.:'))
            c = int(input('Enter The Shift Value.:'))
            bitshiftleft(a,c)
    elif(op=='r'):
            a = int(input('Enter The No.:'))
            c = int(input('Enter The Shift Value.:'))
            bitshiftright(a, c)
    else:
        inv()
#Relational Part:
elif(option=='R'):
    print('MODE: Relational\n')
    a = float(input('Enter the First No. :'))
    b = float(input('Enter the second No. :'))
    rela(a,b)
else:
    inv()





