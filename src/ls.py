import os, sys
if len(sys.argv) > 2:
    locationargs = sys.argv[1]
    ls = "dir "+locationargs
    os.system(ls)
else:
    os.system("dir")