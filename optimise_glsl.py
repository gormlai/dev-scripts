#!/usr/bin/python
#
# This script assumes that you have the following tools somewhere in your path:
# glslangValidator
# spirv-opt
# SPIRV-Cross

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

glslangValidator.exe -V -o ./water_fragment.spv ../shaders/water_fragment.frag

~/glc02/development/opensource/SPIRV-Tools/build/tools/RelWithDebInfo/spirv-opt.exe -O ./terrain_vertex.spv -o ./terr
ain_vertex_opt.spv

~/glc02/development/opensource/SPIRV-Cross/msvc/x64/Release/SPIRV-Cross.exe terrain_vertex_opt.spv --version 430 --ou
tput ./terrain_vertex.vert
