import maya.cmds as base

import Create_Locators
import Create_Joints
import Create_Constraints
import Twist_Loc
import CreateIKH
import Controllers


import importlib


Create_Locators = importlib.reload(Create_Locators)
Create_Joints = importlib.reload(Create_Joints)
Create_Constraints = importlib.reload(Create_Constraints)
Twist_Loc = importlib.reload(Twist_Loc)
CreateIKH = importlib.reload(CreateIKH)
Controllers = importlib.reload(Controllers)


global prefix
global selected



class AutoRigger():
    
    
    def __init__(self):
         self.CreateUI()
        
    

    def CreateUI(self):
        
        base.window("Auto Rigger")
        
        base.rowColumnLayout(adj = True)
        
        base.text(l = "Step 1: Create Locator", w = 100)
        base.separator()
        
        
        base.text(l = "Amount of Spines", w = 100)
        spineJointCount = base.intField(minValue = 1, maxValue = 10, value = 4)
        spineValue = base.intField(spineJointCount, query = True, value = True)
        base.text(l = "Amount of Fingers", w = 100)
        fingerCount = base.intField(minValue = 0, maxValue = 10, value = 5)
        
        
        
        base.button(l="Create Locators", w=200, c="Create_Locators.createLocators("+ str(base.intField(spineJointCount, query = True, value = True))+","+str(base.intField(fingerCount, query = True, value = True))+")")
        base.button(l="Delete Locators", w=200, c="Create_Locators.deleteLocators()")
      
        ##Create_Locators.createField()
        
        
        base.separator()
        base.separator()
  
  
        base.text(l = "Step 2: Twist & Mirroring", w = 100)
        base.button(l="Twist & Reverse Foot Locator Menu", w=200, c="Twist_Loc.LimbTwistLocatorsCreation()") 
        base.button(l="Mirror L -> R", w=200, c="Create_Locators.mirrorLocators(1)")
        base.button(l="Mirror R -> L", w=200, c="Create_Locators.mirrorLocators(-1)")
        base.separator()
        base.separator()
        
        base.text(l = "Step 3: Create Joints", w = 100)
        base.separator()
        base.button(l="Joints Creation Menu", w=200, c="Create_Joints.CreateJointWindows()")
        
        base.separator()
        base.separator()    
      
        base.text(l = "Step 4: Control and Constraint", w = 100)
        base.button(l="Create Controllers", w=200, c="Controllers.CreateController("+ str(base.intField(spineJointCount, query = True, value = True))+","+str(base.intField(fingerCount, query = True, value = True))+")")
        
        base.button(l="Create Constraint", w=200, c="Create_Constraints.CreateConstraints("+ str(base.intField(spineJointCount, query = True, value = True))+","+str(base.intField(fingerCount, query = True, value = True))+")")
        base.separator()
        base.separator()
        
        
        
        
        
        
        base.showWindow()
    
    
    

  