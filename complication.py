from io import StringIO
import sys
import helloworld

stdout = sys.stdout
sys.stdout = stringIO = StringIO()

print("Hello World!")

sys.stdout = stdout
HW = stringIO.getvalue().splitlines()[0]
del stringIO

for i in HW.replace(" ", "").rstrip("!"):
    helloworld.c_helloworld(HW)
