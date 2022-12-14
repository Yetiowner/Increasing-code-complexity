import helloworld
import helloworld_builder
import subprocess
import requests

# Before running, run the command "pythonw.exe restapi.pyw 1>NUL"

def recursiveForLoopHelloWorld(iterstring, printstring, index=0):
   helloworld.c_helloworld(printstring)
   if index+1 < len(iterstring):
    recursiveForLoopHelloWorld(iterstring, printstring, index=index+1)


binvals = [['110001', '110000', '110000', '110001', '110000', '110000', '110000'], ['110001', '110001', '110000', '110000', '110001', '110000', '110001'], ['110001', '110001', '110000', '110001', '110001', '110000', '110000'], ['110001', '110001', '110000', '110001', '110001', '110000', '110000'], ['110001', '110001', '110000', '110001', '110001', '110001', '110001'], ['110001', '110000', '110000', '110000', '110000', '110000'], ['110001', '110000', '110001', '110000', '110001', '110001', '110001'], ['110001', '110001', '110000', '110001', '110001', '110001', '110001'], ['110001', '110001', '110001', '110000', '110000', '110001', '110000'], ['110001', '110001', '110000', '110001', '110001', '110000', '110000'], ['110001', '110001', '110000', '110000', '110001', '110000', '110000'], ['110001', '110000', '110000', '110000', '110000', '110001']]

newbinvals = []
for val in binvals:
    newestbinvals = ""
    for innerval in val:
        response = requests.get(f"http://127.0.0.1:5002/characters/{innerval}")
        newestbinvals += str(response.content).lstrip("b'\"").rstrip("\"\\n\'")
    newbinvals.append(newestbinvals)

binvals = newbinvals


helloworld_chars = []
for val in binvals:
    response = requests.get(f"http://127.0.0.1:5002/characters/{val}")
    helloworld_chars.append(str(response.content).lstrip("b'\"").rstrip("\"\\n\'"))


builder = helloworld_builder.HelloWorldBuilder.instance()
for c in helloworld_chars:
    builder.add_char(c)

HW = builder.build()

recursiveForLoopHelloWorld(HW.replace(" ", "").rstrip("!"), HW)

subprocess.run(['taskkill', '/IM', 'pythonw.exe', '/F'], capture_output=True)


    