import os,platform
print(f'\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')
os.system('git pull')
os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
os.system('clear')
print('\033[1;32m [•] JOIN RANA WhATSAP GROUP')
os.system('xdg-open https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht')
os.system('clear')
rana=platform.architecture()[0]
if rana=="32bit":
    __import__("rana")
elif rana=="64bit":
    __import__("rana1")
