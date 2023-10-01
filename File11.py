import os,platform
print(f'\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')
os.system('git pull')
print('\033[1;32m [•] Join Rana Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht')
 
rana=platform.architecture()[0]
if rana=="32bit":
    __import__("rana")
elif rana=="64bit":
    __import__("rana1")
