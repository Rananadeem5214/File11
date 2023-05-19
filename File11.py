import os,platform
os.system('git pull')

File11=platform.architecture()[0]
if File11=="32bit":
    __import__("rana1")
elif File11=="64bit":
    __import__("rana1")
