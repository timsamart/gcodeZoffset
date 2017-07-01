import numpy as np
import os
import argparse
# loads file in line by line and gives back line array
def load_file_lines(text_file_path):
    text_file = open(text_file_path, 'r')
    lines = text_file.read().split("\n")  # first split by line
    text_file.close()
    return lines

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", help="path to the gcode file", default="E:\\A6\\AA_ww.gcode")
args = vars(ap.parse_args())

zoffset = -0.3
started = False

lines = load_file_lines(args.get("file"))
elementtmp = ""
linestmp = []
for line in lines:
    if line[0:2]=="G0" or line[0:2]=="G1":
        started = True
    if started:
        lineA = line.split(";",1)
        linesa = lineA[0].split(" ")
        for i in range(0, linesa.__len__()):
            if linesa[i].__len__()>0:
                if linesa[i][0] == "Z":
                    znr = float(linesa[i][1:])
                    znr += zoffset
                    linesa[i]="Z{0:.2f}".format(znr)
        linestmp.append(' '.join(linesa))
        if lineA.__len__()>1:
            linestmp[-1]+=(";"+lineA[1])
        if line.__len__()>0:
            if line[0]==";":
                linestmp[-1]+=(";"+lineA[1])
    else:
        linestmp.append(line)

thefile = open('conv.gcode', 'w')
for line in linestmp:
    thefile.write(line+"\n")
