import subprocess
import os
import sys
#subprocess.run(["pip", "install", "wget"])
#import wget
#import zipfile
#url = 'https://nimmaai.tech/data/data.rar'
#filename = wget.download(url)


d = os.path.dirname(__file__)
file=d+"\\install.ttg"
req=d+"\\requirements.txt"
subprocess.run(["pip", "install", "-r",req ])
##with zipfile.ZipFile("data.rar","r") as zip_ref:
    #zip_ref.extractall(d)
##################### changing the txt file to installed ################
g=open(file,'w')
g.write("1")
g.close()
sys.exit()
