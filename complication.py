import cmath

charsout = []

def find_abcs(s):
    chars = []
    for s in ("HelloWorld"):
        code = ord(s)
        x2 = code + 1
        a = 1
        b = code + x2
        c = code * x2
        chars.append((a,b,c))
    return chars

def solve_for_char(a, b, c):
    d = (b**2) - (4*a*c)  
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return chr(min(abs(int(sol1.real)),abs(int(sol2.real))))

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

for char in find_abcs('HelloWorld'):
    charsout.append(solve_for_char(char[0],char[1],char[2]))


for i in convert(charsout):
    print("Hello world!")

