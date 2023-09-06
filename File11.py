import os,platform
os.system('git pull')
print('\033[1;32m [•] Join Rana Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht')
 
trt=platform.architecture()[0]
if trt=="32bit":
    __import__("rana1")
elif trt=="64bit":
    __import__("rana1")
