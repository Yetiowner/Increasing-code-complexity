import helloworld
import helloworld_builder


helloworld_chars = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

builder = helloworld_builder.HelloWorldBuilder()
for c in helloworld_chars:
    builder.add_char(c)

HW = builder.build()
for i in (HW.replace(" ", "").rstrip("!")):
    helloworld.c_helloworld(HW)

    