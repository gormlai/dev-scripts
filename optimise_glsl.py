#!/usr/bin/python
#
# This script assumes that you have the following tools somewhere in your path:
# glslangValidator
# spirv-opt
# SPIRV-Cross

import sys
import os
import ntpath
import time

numArguments = len(sys.argv);
if numArguments!=3:
    print "usage: optimise_glsl.py <source_dir> <destination_dir>"
    exit(0)

srcDir = sys.argv[1]
dstDir = sys.argv[2]


if os.path.isdir(srcDir) == False:
    print " given as source directory, is not a directory."
    exit(0)

if os.path.isdir(dstDir) == False:
    print dstDir + " given as destination directory, is not a directory."
    exit(0)

filelist = os.listdir(srcDir)
for file in filelist:
    name,ext =  os.path.splitext(file)
    if ext==".frag" or ext==".vert" or ext==".comp":
        command = "glslangValidator.exe -V -o " + dstDir +"/" + name +".spv " + srcDir + "/" + file
        os.system(command)

for file in filelist:
    name,ext =  os.path.splitext(file)
    dstFile = dstDir + "/" + name + "_opt.spv"
    srcFile = dstDir + "/" + name + ".spv"
    if os.path.isfile(srcFile):
        optCommand = "spirv-opt.exe -O " + srcFile + " -o " + dstFile
        os.system(optCommand)
        time.sleep(0.1)
        os.remove(srcFile)

for file in filelist:
    name,ext =  os.path.splitext(file)
    dstFile = dstDir + "/" + file
    srcFile = dstDir + "/" + name + "_opt.spv"
    if os.path.isfile(srcFile):
        command = "SPIRV-Cross.exe " + srcFile + " --version 430 --output " + dstFile
        os.system(command)
        time.sleep(0.1)
        os.remove(srcFile)
