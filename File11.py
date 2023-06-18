import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from rana1 import iAmMain
 
        iAmMain().iAmMenu()
 
 
 
elif bit == "32bit":
 
        from rana1 import iAmMain
 
 
        iAmMain().iAmMenu()
 
 
 
