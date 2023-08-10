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
    base.button(l = "Delete Locators", w = 200, c = "Twist_Loc.DeleteTwistNRev()")
    CheckGroup()
    base.showWindow()
    
    
def CheckGroup():
    if base.objExists('TwistNRev'):
        print ('group exists')
    else:
        base.group(em = True, n = "TwistNRev")

    ##setColors()    

def CreateReverseFootroll():

    #L_Heel
    base.select(deselect = True)
    l_rev_Heel = base.spaceLocator(n = "Loc_L_INV_Heel")
    base.scale(0.05, 0.05, 0.05, l_rev_Heel)
    base.move(0.15, -0.5, 0, l_rev_Heel)
    base.parent(l_rev_Heel, 'TwistNRev')
    #R_Heel
    r_rev_Heel = base.spaceLocator(n = "Loc_R_INV_Heel")
    base.scale(0.05, 0.05, 0.05, r_rev_Heel)
    base.move(-0.15, -0.5, 0, r_rev_Heel)
    base.parent(r_rev_Heel, 'TwistNRev')

    #L_toes
    l_toeLoc = base.xform(base.ls("Loc_L_Toes"), q = True, t = True, ws = True)
    l_rev_toes = base.spaceLocator(n = 'Loc_L_INV_Toes')
    base.scale(0.05, 0.05, 0.05, l_rev_toes) 
    base.move(l_toeLoc[0], l_toeLoc[1], l_toeLoc[2], l_rev_toes)
    base.parent(l_rev_toes, 'Loc_L_INV_Heel')
    
    # R_toes
    r_toeLoc = base.xform(base.ls("Loc_R_Toes"), q = True, t = True, ws = True)
    r_rev_toes = base.spaceLocator(n = 'Loc_R_INV_Toes')
    base.scale(0.05, 0.05, 0.05, r_rev_toes) 
    base.move(r_toeLoc[0],r_toeLoc[1], r_toeLoc[2], r_rev_toes)
    base.parent(r_rev_toes, 'Loc_R_INV_Heel')
    
    #foot ball    
    l_rev_ball = base.spaceLocator(n = 'Loc_L_INV_Ball')
    base.scale(0.05, 0.05, 0.05, l_rev_ball)
    base.move(0.15, -0.5, 0.15, l_rev_ball)
    base.parent(l_rev_ball, 'Loc_L_INV_Toes')
    
    #foot ball
    
    r_rev_ball = base.spaceLocator(n = 'Loc_R_INV_Ball')
    base.scale(0.05, 0.05, 0.05, r_rev_ball)
    base.move(-0.15, -0.5, 0.15, r_rev_ball)
    base.parent(r_rev_ball, 'Loc_R_INV_Toes')
    
    #ankle
    
    l_rev_ankle = base.spaceLocator(n = 'Loc_L_INV_Ankle')
    base.scale(0.05, 0.05, 0.05, l_rev_ankle)
    base.move(0.15, -0.4, 0, l_rev_ankle)
    base.parent(l_rev_ankle, 'Loc_L_INV_Ball')
    
     #anklez
    
    r_rev_ankle = base.spaceLocator(n = 'Loc_R_INV_Ankle')
    base.scale(0.05, 0.05, 0.05, r_rev_ankle)
    base.move(-0.15, -0.4, 0, r_rev_ankle)
    base.parent(r_rev_ankle, 'Loc_R_INV_Ball')
        
        
        
def DeleteTwistNRev():
    base.delete(base.ls('TwistNRev'))  