import os 
if os.path.exists("newdc.txt"):
    os.remove("newdc.txt")
else:
    print("file doesnt exist")