import maya.cmds as base
from math import pow, sqrt, cos, acos, radians
   

    
def LimbTwistLocatorsCreation():
    base.window("Limb Twist & Reverse Foot")
    base.rowColumnLayout(nc = 1)
    base.button(l = "Create Reverse Footroll", w = 200, c = "Twist_Loc.CreateReverseFootroll()")
    base.separator(h = 10)
    
    
    base.text("Amount of twist joints", l = "Amount of twist joints")
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

    setColors()    

def CreateReverseFootroll():
    #ankles
    base.select(deselect = True)
    l_rev_Heel = base.spaceLocator(n = "Loc_L_INV_Heel")
    base.scale(0.05, 0.05, 0.05, l_rev_Heel)
    base.move(0.15, 0, 0, l_rev_Heel)
    base.parent(l_rev_Heel, 'TwistNRev')
    
    r_rev_Heel = base.spaceLocator(n = "Loc_R_INV_Heel")
    base.scale(0.05, 0.05, 0.05, r_rev_Heel)
    base.move(-0.15, 0, 0, r_rev_Heel)
    base.parent(r_rev_Heel, 'TwistNRev')
    # toes
    l_toeLoc = base.xform(base.ls("Loc_L_Toes"), q = True, t = True, ws = True)
    l_rev_toes = base.spaceLocator(n = 'Loc_L_INV_Toes')
    base.scale(0.05, 0.05, 0.05, l_rev_toes) 
    base.move(l_toeLoc[0], l_toeLoc[1], l_toeLoc[2], l_rev_toes)
    base.parent(l_rev_toes, 'Loc_L_INV_Heel')
    
    # toes
    r_toeLoc = base.xform(base.ls("Loc_R_Toes"), q = True, t = True, ws = True)
    r_rev_toes = base.spaceLocator(n = 'Loc_R_INV_Toes')
    base.scale(0.05, 0.05, 0.05, r_rev_toes) 
    base.move(r_toeLoc[0],r_toeLoc[1], r_toeLoc[2], r_rev_toes)
    base.parent(r_rev_toes, 'Loc_R_INV_Heel')
    
    #foot ball    
    l_ballLoc = base.xform(base.ls("Loc_L_Ball"), q = True, t = True, ws = True)    
    l_rev_ball = base.spaceLocator(n = 'Loc_L_INV_Ball')
    base.scale(0.05, 0.05, 0.05, l_rev_ball)
    base.move(l_ballLoc[0], l_ballLoc[1], l_ballLoc[2], l_rev_ball)
    base.parent(l_rev_ball, 'Loc_L_INV_Toes')
    
    #foot ball
    r_ballLoc = base.xform(base.ls("Loc_R_Ball"), q = True, t = True, ws = True)    
    r_rev_ball = base.spaceLocator(n = 'Loc_R_INV_Ball')
    base.scale(0.05, 0.05, 0.05, r_rev_ball)
    base.move(r_ballLoc[0], r_ballLoc[1], r_ballLoc[2], r_rev_ball)
    base.parent(r_rev_ball, 'Loc_L_INV_Toes')
    
    #ankle
    l_ankleLoc = base.xform(base.ls("Loc_L_Foot"), q = True, t = True, ws = True)
    l_rev_ankle = base.spaceLocator(n = 'Loc_L_INV_Ankle')
    base.scale(0.05, 0.05, 0.05, l_rev_ankle)
    base.move(l_ankleLoc[0], l_ankleLoc[1],l_ankleLoc[2], l_rev_ankle)
    base.parent(l_rev_ankle, 'Loc_L_INV_Ball')

    r_ankleLoc = base.xform(base.ls("Loc_R_Foot"), q = True, t = True, ws = True)    
    r_rev_ankle = base.spaceLocator(n = 'Loc_R_INV_Ankle')
    base.scale(0.05, 0.05, 0.05, r_rev_ankle)
    base.move(r_ankleLoc[0], r_ankleLoc[1], r_ankleLoc[2], r_rev_ankle)
    base.parent(r_rev_ankle, 'Loc_R_INV_Ball')

    
    
    
def CreateForearmTwist(amount):
    
    
    
    base.select(deselect = True)
    global armTwist
    print (amount)
   
    L_elbowPos = base.xform(base.ls('Loc_L_Elbow'), q = True, t = True, ws = True)
    L_wristPos = base.xform(base.ls('Loc_L_Wrist'), q = True, t = True, ws = True)
    
    L_vectorX =  L_wristPos[0] - L_elbowPos[0]
    L_vectorY = L_wristPos[1] - L_elbowPos[1]
    L_vectorZ = L_wristPos[2] - L_elbowPos[2]
  

   
    for i in range(amount - 1):

        twistLoc = base.spaceLocator(n = 'Loc_L_ArmTwist_'+str(i))
        base.move(L_elbowPos[0] + (L_vectorX / amount) + ((L_vectorX / amount) * i), L_elbowPos[1] + (L_vectorY / amount) + ((L_vectorY / amount) * i), L_elbowPos[2] + (L_vectorZ / amount) + ((L_vectorZ / amount) * i), twistLoc)
        base.scale(0.05, 0.05, 0.05, twistLoc)
        base.parent(twistLoc, 'TwistNRev')
              
    R_elbowPos = base.xform(base.ls('Loc_R_Elbow'), q = True, t = True, ws = True)
    R_wristPos = base.xform(base.ls('Loc_R_Wrist'), q = True, t = True, ws = True)
    
    R_vectorY = R_wristPos[1] - R_elbowPos[1]
    R_vectorX =  R_wristPos[0] - R_elbowPos[0]
    R_vectorZ = R_wristPos[2] - R_elbowPos[2]
   
    for j in range(amount - 1):

        r_twistLoc = base.spaceLocator(n = 'Loc_R_ArmTwist_'+str(j))
        base.move(R_elbowPos[0] + (R_vectorX / amount) + ((R_vectorX / amount) * j), R_elbowPos[1] + (R_vectorY / amount) + ((R_vectorY / amount) * j), R_elbowPos[2] + (R_vectorZ / amount) + ((R_vectorZ / amount) * j), r_twistLoc)
        base.scale(0.05, 0.05, 0.05, r_twistLoc)
        base.parent(r_twistLoc, 'TwistNRev')

def setColors():
    base.setAttr('TwistNRev.overrideEnabled', 1)
    base.setAttr('TwistNRev.overrideRGBColors', 1)
    base.setAttr('TwistNRev.overrideColorRGB', 1,1,1)       



def DeleteTwistNRev():
    base.delete(base.ls('TwistNRev'))
      