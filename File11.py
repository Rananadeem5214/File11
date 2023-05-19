import os,platform
os.system('git pull')

File11=platform.architecture()[0]
if File11=="32bit":
    print('Sorry Update Your Phone...')
elif File11=="64bit":
    __import__("rana")
