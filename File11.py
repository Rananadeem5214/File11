import os,platform
print(f'\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')
os.system('git pull')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system("pkg install espeak") 
print('\033[1;32m [•] Join Rana Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht')
 
trt=platform.architecture()[0]
if trt=="32bit":
    __import__("rana1")
elif trt=="64bit":
    __import__("rana1")
