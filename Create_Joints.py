import maya.cmds as base





def createJoints():
    if base.objExists('RIG'):
        print('RIG Exists')
    else:
        jointGRP = base.group(em=True, name='RIG')

        ## Create Spine

        root = base.ls("Loc_ROOT")

        allSpines = base.ls("Loc_SPINE_*", type='locator')
        spine = base.listRelatives(*allSpines, p=True, f=True)
        


        rootPos = base.xform(root, q=True, t=True, ws=True)
        rootJoint = base.joint(radius=0.1, p=rootPos, name='RIG_TOOL')
        
        
        base.parent(rootJoint, w = True, a = True)
        base.parent(rootJoint,'RIG', a = True)
         
        
        for i,s in enumerate(spine):
            pos = base.xform(s, q = True, t = True, ws = True)
            j = base.joint(radius = 0.08, p = pos, name = "RIG_SPINE_" + str(i))
            
            
        ## Create Arm
        
        L_UpperArm = base.ls('Loc_L_UpperArm')
        L_UpperArmPos = base.xform(L_UpperArm, q = True, t = True, ws = True)
        L_UpperArmJoint = base.joint(radius = 0.1, p = L_UpperArmPos, name = "RIG_L_UpperArm")
        
        
        
        
        
        ## Create Elbow
        
        L_Elbow = base.ls('Loc_L_Elbow')
        L_ElbowPos = base.xform(L_Elbow, q = True, t = True, ws = True)
        L_ElbowJoint = base.joint(radius = 0.1, p = L_ElbowPos, name = "RIG_L_Elbow")
        
        
        
        ## Create Hand
        
        
        
        L_Wrist = base.ls('Loc_L_Wrist')
        L_WristPos = base.xform(L_Wrist, q = True, t = True, ws = True)
        L_WristJoint = base.joint(radius = 0.1, p = L_WristPos, name = "RIG_L_Wrist")
        
        
        
        
        
       
         
        
        
        