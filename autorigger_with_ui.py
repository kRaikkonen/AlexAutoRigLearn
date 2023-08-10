import maya.cmds as base

import Create_Locators
import Create_Joints
import Create_Constraints
import Twist_Loc
import CreateIKH


import importlib


Create_Locators = importlib.reload(Create_Locators)
Create_Joints = importlib.reload(Create_Joints)
Create_Constraints = importlib.reload(Create_Constraints)
Twist_Loc = importlib.reload(Twist_Loc)
CreateIKH = importlib.reload(CreateIKH)

global prefix
global selected



class AutoRigger():
    
    
    def __init__(self):
         self.CreateUI()
        
    

    def CreateUI(self):
        
        base.window("Auto Rigger")
        
        base.rowColumnLayout(nc=2)
        
        
        
        
        
        base.button(l="Create Locators", w=200, c="Create_Locators.createLocators()")
        base.button(l="Delete Locators", w=200, c="Create_Locators.deleteLocators()")
        base.separator()
        base.separator()
        Create_Locators.createField()
        base.separator()
        base.separator()
        base.button(l="Mirror L -> R", w=200, c="Create_Locators.mirrorLocators(1)")
        base.button(l="Mirror R -> L", w=200, c="Create_Locators.mirrorLocators(-1)")
        base.separator()
        base.separator()
        base.button(l="Joints Creation Menu", w=200, c="Create_Joints.CreateJointWindows()")
        base.button(l="Twist & Reverse Foot Menu", w=200, c="Twist_Loc.LimbTwistLocatorsCreation()")     
      
        base.button(l="Create Constraint", w=200, c="Create_Constraints.createConstraint()")
        base.separator()
        base.separator()
        
        
        
        
        
        
        base.showWindow()
    
    
    
AutoRigger()
  