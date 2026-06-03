import sys
x = len(sys.argv)
print(x)
print(sys.argv[0])
#print(sys.argv[1])
"""What does sys.argv[0] represent when a command is run to refer to this file as:
Python testargs.py Hello"""
print(f"system is {sys.platform}")
print(f"python version is {sys.version}")
sys.exit()
print(f"python version is {sys.version}")
print("hello world")