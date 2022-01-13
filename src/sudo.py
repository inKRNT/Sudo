
import os, sys
if len(sys.argv) < 2:
    sys.argv.append('cmd')
    def agrvma():
        if sys.argv[1] == "cmd":
            return "cmd"
        elif sys.argv[1] == "wt":
            return "wt"
        elif sys.argv[1] == "":
            return "cmd"
        elif sys.argv[1] == None:
            return "'/k cd /d %CD% && %*'"
        else:
            return "cmd"
    def agrvmal():
        if sys.argv[1] == "cmd":
            return "'/k cd /d %CD% && %*'"
        elif sys.argv[1] == "wt":
            print("Please make sure it is in your PATH")
            return "wt"
        elif sys.argv[1] == "":
            return "'/k cd /d %CD% && %*'"
        elif sys.argv[1] == None:
            return "'/k cd /d %CD% && %*'"
        else:
            return 
    typ_of = agrvma()
    argfun = """@echo off"""
    arg2p5p5 = agrvmal()	
    arg2p5 = '"Start-Process '+str(typ_of)+' -Verb RunAs -ArgumentList '+str(arg2p5p5)+'"'
    arg2 = "powershell -Command "+str(arg2p5)
    def sudo():
        os.system("@echo off")
        os.system(arg2)
        os.system("@echo on")
    sudo()
else:
    if sys.argv[1] == "wt --add-to-path":
        print("""How to add Preview Windows Terminal to PATH
        set one type set | PATH=%PATH%; ( and one of these """+str(os.system("echo %userprofile%\\appdata\\local\\Microsoft\\WindowsApps\\wt.exe "))+""" |""")
    else:
        def agrvma():
            if sys.argv[1] == "cmd":
                return "cmd"
            elif sys.argv[1] == "wt":
                return "wt"
            elif sys.argv[1] == "":
                return "cmd"
            elif sys.argv[1] == None:
                return "'/k cd /d %CD% && %*'"
            else:
                return "cmd"
        def agrvmal():
            if sys.argv[1] == "cmd":
                return "'/k cd /d %CD% && %*'"
            elif sys.argv[1] == "wt":
                wt_dir = os.system("echo %USERPROFILE% ")
                wt_dir_path = os.system("where /r C: wt.exe")
                wt_1 = str(wt_dir_path).splitlines()
                os.system("cls")
                wt = str("").join(str(wt_1[0]))
                print("Please make sure it is in your PATH type {PATH = %PATH%; %USERPROFILE%\\appdata\\local\\Microsoft\\WindowsApps\\wt.exe } to add")
                return "wt"
            elif sys.argv[1] == "":
                return "'/k cd /d %CD% && %*'"
            elif sys.argv[1] == None:
                return "'/k cd /d %CD% && %*'"
            else:
                return 
        typ_of = agrvma()
        argfun = """@echo off"""
        arg2p5p5 = agrvmal()	
        arg2p5 = '"Start-Process '+str(typ_of)+' -Verb RunAs -ArgumentList '+str(arg2p5p5)+'"'
        arg2 = "powershell -Command "+str(arg2p5)
        def sudo():
            os.system("@echo off")
            os.system(arg2)
            os.system("@echo on")
        sudo()
