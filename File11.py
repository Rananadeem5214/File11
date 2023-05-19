import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from File11 import File11
 
        menu()
 
 
 
elif bit == "32bit":
 
        from File11 import File11
 
 
        menu()
 
 
 
