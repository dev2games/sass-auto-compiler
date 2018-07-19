# Python is awesome
#@author Nelson Sanchez

import os
import sys
import threading

# Arguments
args = {
    "directory": "",
    "output": "",
    "optimization": ""
}


# Runs the code continuously every 2 seconds
def init():
    threading.Timer(1.0, init).start()
    # Do not run if the initial arguments are undefined
    print("Hello World")

def createDirectory(dir):
    # Checks if the directory exists
    if not os.path.isdir(dir) or not os.path.exists(dir):
        createDir = ""
        while not createDir:
            createDir = input("Directory does not exist. Create it now? [y/n]").lower()
    if createDir == "y":
        print("Directory has been created!")
        os.mkdir(dir)
    else:
        print("Exiting program, directory does not exist at: " + dir)
        sys.exit()



while not args["directory"]:
    args["directory"] = input("Please enter your sass directory folder: [/home/dev2games/Desktop/project/sass/]")
    createDirectory(args["directory"])

while not args["output"]:
    args["output"] = input("Please enter the output directory for the style.css: [/home/dev2games/Desktop/project/css/]")

while args["optimization"] != 'n' and args["optimization"] != 'y':
    args["optimization"] = input("(Optimization) Will your sass folder have subdirectories? [y/n]: ").lower()

print("Perform some function")

init()
