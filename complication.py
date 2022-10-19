from io import StringIO
import sys

stdout = sys.stdout
sys.stdout = stringIO = StringIO()

print("HelloWorld")

sys.stdout = stdout
helloWorld = stringIO.getvalue().splitlines()[0]
del stringIO

for i in helloWorld:
    print("Hello world!")
