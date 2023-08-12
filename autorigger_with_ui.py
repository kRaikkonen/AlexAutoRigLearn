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

CreateIKH = importlib.reload(CreateIKH)
Controllers = importlib.reload(Controllers)


global prefix
global selected



class AutoRigger():
    
    
    def __init__(self):
         self.CreateUI()
        
    

    def CreateUI(self):
        
        base.window("Alex Auto Rigger")
        
        base.rowColumnLayout(adj = True)
        
        
        
        base.separator(st = 'none')   
        #base.text(l='Prefix', w=200, fn='boldLabelFont', bgc=[1, 0.5, 0])  # 设置字体样式为粗体，背景颜色为橘色
        #self.prefix = base.textFieldGrp(w = 200, text = 'Put Your RIG Prefix Here', editable = True)
        base.separator(h=10)  
           
        base.text(l = "Step 1: Create Locator", w = 100, fn='boldLabelFont', bgc=[1, 0.5, 0])
        base.separator(h = 5, st = 'none')
        
        #Sliders 4 Loc Stats
        
        self.spineJointCount = base.intSliderGrp(l = "Spine Count", min = 1, max = 10, value = 4, step = 1, field = True)
        self.fingerCount = base.intSliderGrp(l = "Finger Count", min = 1, max = 10, value = 5, step = 1, field = True)
        
        base.separator(h = 2, st = 'none') 
        
        
        #Double ELB
        #self.doubleElbow = base.checkBox(l = 'Double Elbow', align = 'left' )   
        
        base.separator(h = 10, st = 'none') 
        base.button(l = "Create Locators", w = 200, c = self.DoLocators)
        base.button(l="Twist & Reverse Foot Locator Menu", w=200, c="Twist_Loc.TwistNreverse()") 
        
        base.button(l="Delete All Locators", w=200, c="Create_Locators.deleteLocators()")
        base.separator(st = 'none') 
        
       
        
        
      
        
        
        
        base.separator(st = 'none')   
        base.separator(st = 'none')   
  
        base.separator(h=10)  
        
        base.text(l = "Step 2: Move Locs & Mirroring", w = 100 , fn='boldLabelFont', bgc=[1, 0.5, 0])
        
        base.separator(h = 5, st = 'none')
        
        base.button(l="Mirror L -> R", w=200, c="Create_Locators.mirrorLocators(1)")
        base.button(l="Mirror R -> L", w=200, c="Create_Locators.mirrorLocators(-1)")
          
        
        base.separator(h=10) 
        
        base.text(l = "Step 3: Create Joints", w = 100 , fn='boldLabelFont', bgc=[1, 0.5, 0])
        base.separator(h = 5, st = 'none')
           
        base.button(l="Joints Creation Menu", w=200, c="Create_Joints.CreateJointWindows()")
        
        base.separator(h=10)       
      
        base.text(l = "Step 4: Control and Constraint", w = 100 , fn='boldLabelFont', bgc=[1, 0.5, 0])
        
        base.separator(h = 5, st = 'none')
        
        base.button(l = "Controller Constraint", w = 200, c = self.FinalizeRig)
        
        
        base.separator(h=10)       
      
        base.text(l = "Step 5: Bind Skin", w = 100 , fn='boldLabelFont', bgc=[1, 0.5, 0])
        
        base.separator(h = 5, st = 'none')
        
        base.button(l = "Bind Skin", w = 200, c = "Create_Constraints.BindSkin()")
        
        
        
        
        
        base.showWindow()
    
    def DoLocators(self, void):
        temp_spineCount = base.intSliderGrp(self.spineJointCount, q = True, v = True)
        temp_fingerCount = base.intSliderGrp(self.fingerCount, q = True, v = True)
        #_doubleElbow = base.checkBox(self.doubleElbow, q = True, v = True)
        Create_Locators.createLocators(temp_spineCount, temp_fingerCount)    
 
    def FinalizeRig(self, void):
    
        _spineCount = base.intSliderGrp(self.spineJointCount, q = True, v = True)
        _fingerCount = base.intSliderGrp(self.fingerCount, q = True, v = True) 
        Controllers.CreateController(_spineCount, _fingerCount)
        CreateIKH.IKHandles()
        Create_Constraints.CreateConstraints(_spineCount,_fingerCount)  

  