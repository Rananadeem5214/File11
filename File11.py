import os,platform
rana=platform.architecture()[0]
if rana=="32bit":
    __import__("rana")
elif rana=="64bit":
    __import__("rana1")
