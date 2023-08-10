import maya.cmds as base
from math import pow, sqrt, cos, acos, radians

def LimbTwistLocatorsCreation():
    base.window("Limb Twist & Reverse Foot")
    base.rowColumnLayout(nc = 1)
    base.button(l = "Create Reverse Footroll", w = 200, c = "Twist_Loc.CreateReverseFootroll()")
    base.separator(h = 10)
    base.text("Twist Amount", l = "Amount of twist joints")
    armTwist = base.intField(minValue = 2, maxValue = 10, value = 3)
    base.button(l = "Create Forearm Twist", w = 200,  c = "Twist_Loc.CreateForearmTwist("+str(base.intField(armTwist, query = True, value = True))+")")
    base.separator(h = 10)
    base.button(l = "Delete Locators", w = 200, c = "DeleteTwistNRev()")
    CheckGroup()
    base.showWindow()
    
    
def CheckGroup():
    if base.objExists('TwistNRev'):
        print ('group exists')
    else:
        base.group(em = True, n = "TwistNRev")

    ##setColors()    

def CreateReverseFootroll():

    #ankles
    base.select(deselect = True)
    l_rev_ankle = base.spaceLocator(n = "Loc_L_INV_Heel")
    base.scale(0.05, 0.05, 0.05, l_rev_ankle)
    base.move(0.15, -0.5, 0, l_rev_ankle)
    base.parent(l_rev_ankle, 'TwistNRev')

        
        
        
def DeleteTwistNRev():
    base.delete(base.ls('TwistNRev'))  