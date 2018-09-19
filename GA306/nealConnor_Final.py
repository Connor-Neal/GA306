import maya.cmds as cmds

def create_staircase (presize_h=1, presize_w=5, presize_d=5, cubeclone=5):
    yposition = 0.5
    zposition = 0.5
   
    for i in range(5):
        mystair = cmds.polyCube( h=presize_h, w=presize_w, d=presize_d)
        cmds.move( 0, yposition, zposition, mystair)
        yposition += 1
        zposition += 2.5

create_staircase(cubeclone=5)