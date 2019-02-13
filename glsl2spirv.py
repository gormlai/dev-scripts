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
    print "usage: glsl2spirv.py <source_dir> <destination_dir>"
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
    srcFile = srcDir + "/" + file
    dstFile = dstDir + "/" + ext[1:] + ".spv"
    if os.path.isfile(srcFile):
        if os.path.isfile(dstFile):
            os.remove(dstFile)
        time.sleep(0.1)
        command = "glslangValidator.exe " + srcFile + " -V110 --target-env vulkan1.1 -o " + dstFile
        print command
        os.system(command)
