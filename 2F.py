import os,platform
os.system('git pull')
print('\033[1;32m [✓] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/CGM6VPP6ILAHpp88PTiZ79')
rana=platform.architecture()[0]
if rana=="32bit":
    __import__("R2F")
elif rana=="64bit":
    __import__("R2F")
