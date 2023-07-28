import maya.cmds as base
import importlib
import Create_Locators
import Create_Joints




Create_Locators = importlib.reload(Create_Locators)
Create_Joints = importlib.reload(Create_Joints)







base.window("Auto Rigger")

base.rowColumnLayout(nc=2)





base.button(l="Create Locators", w=200, c="Create_Locators.createLocators()")
base.button(l="Delete Locators", w=200, c="deleteLocators()")
base.button(l="Mirror L -> R", w=200, c="mirrorLocators(1)")
base.button(l="Mirror R -> L", w=200, c="mirrorLocators(-1)")
base.button(l="Create Joints", w=200, c="Create_Joints.createJoints()")
base.separator()

Create_Locators.createField()




base.showWindow()






############################## ACTUAL CODE #########################################

########################
### Pelvis Functions ###
########################


            
def mirrorLocators(side):
    allLeftLocators = base.ls("Loc_L_*")
    LeftLocators = base.listRelatives(*allLeftLocators, p=True, f=True)
    
    allRightLocators = base.ls("Loc_R_*")
    RightLocators = base.listRelatives(*allRightLocators, p=True, f=True)
   
    if side == 1:
        for i,l in enumerate(LeftLocators):
            pos = base.xform(l, q = True, t =True,ws = True)
            base.move(-pos[0],pos[1],pos[2],RightLocators[i])
    else:
        for i,l in enumerate(RightLocators):
            pos = base.xform(l, q = True, t =True,ws = True)
            base.move(-pos[0],pos[1],pos[2],LeftLocators[i])
        
       
    
def deleteLocators():
    nodes = base.ls("Loc_*")
    base.delete(nodes)
