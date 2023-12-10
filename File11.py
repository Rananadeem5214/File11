import os,platform
os.system('git pull')
os.system('pkg install espeak')
print('\033[1;32m [+] JOIN RANA WhATSAP GROUP')
os.system('xdg-open https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht')
rana=platform.architecture()[0]
if rana=="32bit":
    __import__("rana")
elif rana=="64bit":
    __import__("rana1")
