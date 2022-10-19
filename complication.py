HW = "Hello World!\n"
for i in (HW.replace(" ", "").rstrip("!\n")):
    for y in HW:
        print(y, end="")

