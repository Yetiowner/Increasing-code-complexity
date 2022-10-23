import helloworld
import helloworld_builder
import subprocess
import requests

# Before running, run the command "pythonw.exe restapi.pyw 1>NUL"

binvals = ['1001000', '1100101', '1101100', '1101100', '1101111', '100000', '1010111', '1101111', '1110010', '1101100', '1100100', '100001']
helloworld_chars = []
for val in binvals:
    response = requests.get(f"http://127.0.0.1:5002/characters/{val}")
    helloworld_chars.append(str(response.content).lstrip("b'\"").rstrip("\"\\n\'"))


builder = helloworld_builder.HelloWorldBuilder.instance()
for c in helloworld_chars:
    builder.add_char(c)

HW = builder.build()
for i in (HW.replace(" ", "").rstrip("!")):
    helloworld.c_helloworld(HW)

subprocess.run(['taskkill', '/IM', 'pythonw.exe', '/F'], capture_output=True)


    