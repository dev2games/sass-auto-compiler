#Python is awesome

#Arguments
directory = ""
output = ""
optimization = ""

while not directory:
    directory = input("Please enter your sass directory folder: [/home/dev2games/Desktop/project/sass/]")

while not output:
    output = input("Please enter the output directory for the style.css: [/home/dev2games/Desktop/project/css/]")

while optimization != 'n' and optimization != 'y':
    optimization = input("(Optimization) Will your sass folder have subdirectories? [y/n]: ").lower()


print("Perform some function")

