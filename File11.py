import os, platform, time, sys
os.system('pkg install espeak -y')
os.system('xdg-open https://chat.whatsapp.com/E8OceeMUihl8YXyJsng4XX')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
 
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
ranaxd = platform.architecture()[0]
if ranaxd == '64bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit')
 import rana1
elif ranaxd == '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is 32bit')
 import rana
