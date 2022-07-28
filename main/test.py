import subprocess
import os
d = os.path.dirname(__file__)
print(d)
v=d+"\\volume.py"
print(v)
subprocess.call("start cmd /c "+v, shell=True)
print("hrllo")
