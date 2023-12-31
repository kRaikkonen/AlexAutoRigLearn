import maya.cmds as base

def CreateController(spineCount, fingerCount):
    
    CreateMaster()
    CreatePelvis()
    CreateWrists()

    createFeet()
    CreateSpines(spineCount)
    CreateClavicles(spineCount)
    CreateNeck(spineCount)
    CreateHead()
    CreateFingers(fingerCount)
    setColors()
    
def CreateMaster():
    ## master
    master_ctrl = base.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 16, name = "Main_CTRL")
    selection = base.select("Main_CTRL.cv[1]","Main_CTRL.cv[3]","Main_CTRL.cv[5]","Main_CTRL.cv[7]","Main_CTRL.cv[9]","Main_CTRL.cv[11]","Main_CTRL.cv[13]","Main_CTRL.cv[15]")
    base.scale(0.7, 0.7, 0.7, selection)
    base.scale(2, 2, 2, master_ctrl)

    base.makeIdentity(master_ctrl, apply = True, t = 1, r = 1, s = 1)
    
def CreatePelvis():
    ## pelvis
    pelvis_ctrl = base.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 8, name = "CTRL_PELVIS")
    rootPos = base.xform(base.ls("RIG_ROOT", type = 'joint'), q = True, t = True, ws = True)
    base.move(rootPos[0],rootPos[1],rootPos[2], pelvis_ctrl) 
    base.scale(0.5, 0.5, 0.5, pelvis_ctrl)   
    base.makeIdentity(pelvis_ctrl, apply = True, t = 1, r = 1, s = 1)  
    base.parent(pelvis_ctrl, "Main_CTRL")       
    
def CreateWrists():    

    #left
    L_wrist_ctrl = base.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 16, name = "CTRL_L_Wrist")
    base.addAttr(shortName = "PV", longName = "Elbow_PV", attributeType = 'double', defaultValue = 0, minValue = -100, maxValue = 100, keyable = True)
    l_selection = base.select("CTRL_L_Wrist.cv[1]","CTRL_L_Wrist.cv[3]","CTRL_L_Wrist.cv[5]","CTRL_L_Wrist.cv[7]","CTRL_L_Wrist.cv[9]","CTRL_L_Wrist.cv[11]","CTRL_L_Wrist.cv[13]","CTRL_L_Wrist.cv[15]")
    
    base.scale(0.7, 0.7, 0.7, l_selection)
    base.scale(0.15, 0.15, 0.15, L_wrist_ctrl)
    
    l_wristPos = base.xform(base.ls("RIG_L_Wrist"), q = True, t = True, ws = True)
    l_wristRot = base.joint(base.ls("RIG_L_Wrist"), q = True, o = True)
    
    base.move(l_wristPos[0], l_wristPos[1], l_wristPos[2], L_wrist_ctrl)
    base.rotate(0, 0, l_wristRot[0], L_wrist_ctrl)
    
    base.makeIdentity(L_wrist_ctrl, apply = True, t = 1, r = 1, s = 1)
    base.parent(L_wrist_ctrl, "Main_CTRL")
    
    #right
    R_wrist_ctrl = base.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 16, name = "CTRL_R_Wrist")
    base.addAttr(shortName = "PV", longName = "Elbow_PV", attributeType = 'double', defaultValue = 0, minValue = -100, maxValue = 100, keyable = True)    
    r_selection = base.select("CTRL_R_Wrist.cv[1]","CTRL_R_Wrist.cv[3]","CTRL_R_Wrist.cv[5]","CTRL_R_Wrist.cv[7]","CTRL_R_Wrist.cv[9]","CTRL_R_Wrist.cv[11]","CTRL_R_Wrist.cv[13]","CTRL_L_Wrist.cv[15]")
    
    base.scale(0.7, 0.7, 0.7, r_selection)
    base.scale(0.15, 0.15, 0.15, R_wrist_ctrl)
    
    r_wristPos = base.xform(base.ls("RIG_R_Wrist"), q = True, t = True, ws = True)
    r_wristRot = base.joint(base.ls("RIG_R_Wrist"), q = True, o = True)
    
    base.move(r_wristPos[0], r_wristPos[1], r_wristPos[2], R_wrist_ctrl)
    base.rotate(0, 0, r_wristRot[0], R_wrist_ctrl)
    
    base.makeIdentity(R_wrist_ctrl, apply = True, t = 1, r = 1, s = 1)
    base.parent(R_wrist_ctrl, "Main_CTRL")
    
    
def CreateClavicles(spineCount):
    l_clavicle = base.curve(p = [(1,0,0),(1,1,1), (1,1.5,2), (1,1.7,3), (1,1.5,4), (1,1,5), (1,0,6), (-1, 0,6), (-1,1,5), (-1,1.5,4), (-1,1.7,3), (-1,1.5,2), (-1,1,1), (-1,0,0) ], degree = 1, name = "CTRL_L_Clavicle")
    r_clavicle = base.curve(p = [(1,0,0),(1,1,1), (1,1.5,2), (1,1.7,3), (1,1.5,4), (1,1,5), (1,0,6), (-1, 0,6), (-1,1,5), (-1,1.5,4), (-1,1.7,3), (-1,1.5,2), (-1,1,1), (-1,0,0) ], degree = 1, name = "CTRL_R_Clavicle")
    
    base.scale(0.05, 0.05, 0.05, l_clavicle)    
    base.scale(0.05, 0.05, 0.05, r_clavicle)  
    
    l_ArmPos = base.xform(base.ls("RIG_L_UpperArm"), q = True, t = True, ws = True)  
    r_ArmPos = base.xform(base.ls("RIG_R_UpperArm"), q = True, t = True, ws = True)
    
    l_claviclePos = base.xform(base.ls("RIG_L_Clavicle"), q = True, t = True, ws = True)
    r_claviclePos = base.xform(base.ls("RIG_R_Clavicle"), q = True, t = True, ws = True)
    
    base.move(l_ArmPos[0], l_ArmPos[1] + 0.125, l_ArmPos[2] - 0.1, l_clavicle)
    base.move(r_ArmPos[0], r_ArmPos[1] + 0.125, r_ArmPos[2] - 0.1, r_clavicle)
    
    base.move(l_claviclePos[0],l_claviclePos[1],l_claviclePos[2], l_clavicle+".scalePivot", l_clavicle+".rotatePivot")    
    base.move(r_claviclePos[0],r_claviclePos[1],r_claviclePos[2], r_clavicle+".scalePivot", r_clavicle+".rotatePivot") 

    base.makeIdentity(l_clavicle, apply = True, t = 1, r = 1, s = 1)
    base.makeIdentity(r_clavicle, apply = True, t = 1, r = 1, s = 1)
    
    base.parent(l_clavicle, "CTRL_SPINE_"+str(spineCount - 1))
    base.parent(r_clavicle, "CTRL_SPINE_"+str(spineCount - 1))

def CreateSpines(spineCount):
    
    for i in range(0, spineCount):
        spinePos = base.xform(base.ls("RIG_SPINE_"+str(i)), q = True, t = True, ws = True)
        spine = base.curve(p =[(0, spinePos[1], spinePos[2]), (0, spinePos[1], spinePos[2] - 1), (0, spinePos[1] + 0.1, spinePos[2] - 1.1), (0, spinePos[1] + 0.1, spinePos[2] - 1.4), (0, spinePos[1] - 0.1, spinePos[2] - 1.4), (0, spinePos[1] - 0.1, spinePos[2] - 1.1), (0, spinePos[1], spinePos[2] - 1)], degree = 1, name = "CTRL_SPINE_"+str(i))
        base.move(spinePos[0], spinePos[1], spinePos[2], spine+".scalePivot", spine+".rotatePivot")
        if (i == 0):
            base.parent(spine, "CTRL_PELVIS")
        else:
            base.parent(spine, "CTRL_SPINE_"+str(i-1))    
      
def CreateNeck(spineCount):
    neck = base.curve(p = [(0.5,0,0), (0.25, -0.25, -0.5), (-0.25, -0.25, -0.5), (-0.5,0,0), (-0.25, -0.25, 0.5), (0.25, -0.25, 0.5), (0.5, 0,0)], degree = 1, name = "CTRL_NECK")
    neckPos = base.xform(base.ls("RIG_Neck_Start"), q = True, t = True, ws = True)
    base.scale(0.5, 0.5, 0.5, neck)
    base.move(neckPos[0], neckPos[1]+0.1, neckPos[2], neck)
    base.move(neckPos[0], neckPos[1], neckPos[2], neck+".scalePivot", neck+".rotatePivot")
    base.parent(neck, "CTRL_SPINE_"+str(spineCount-1))
    
    base.makeIdentity(neck, apply = True, t = 1, r = 1, s = 1)
 
def CreateHead():    
    head = base.curve(p = [(0.5,0,0), (0.25,-0.25,-0.5), (0.25,-0.5, -0.5), (0,-0.6,-0.5),(-0.25,-0.5,-0.5), (-0.25, -0.25, -0.5), (-0.5,0,0), (-0.25, -0.25, 0.5), (-0.25, -0.5, 0.5), (0,-0.6, 0.5) ,(0.25, -0.5, 0.5),(0.25, -0.25, 0.5), (0.5,0,0)], degree = 1, name = "CTRL_HEAD")
    base.scale(0.5, 0.5, 0.5, head)
    headPos = base.xform(base.ls("RIG_Head"), q= True, t = True, ws = True)
    neckPos = base.xform(base.ls("RIG_Neck_End"), q = True, t = True, ws = True)
    base.move(headPos[0], headPos[1], headPos[2], head)
    base.move(neckPos[0], neckPos[1], neckPos[2], head+".scalePivot", head+".rotatePivot")    
    base.parent(head, "CTRL_NECK")
    base.makeIdentity(head, apply = True, t = 1, r = 1, s = 1)    
     #jaw
    jaw = base.curve(p = [(0,0,0),(0.1, 0.1, 0), (0, 0.2,0), (-0.1, 0.1,0), (0,0,0)], degree = 1, name = "CTRL_JAW")
    base.move(0, 0.1, 0, jaw+".scalePivot", jaw+".rotatePivot")
    base.scale(0.3, 0.3, 0.3, jaw)
    jawPos = base.xform(base.ls("RIG_Jaw_End"), q = True, t = True, ws = True)
    jawStart = base.xform(base.ls("RIG_Jaw_Start"), q = True, t = True, ws = True)
    base.move(jawPos[0], jawPos[1] - 0.1, jawPos[2] + 0.1, jaw)
    base.move(jawStart[0], jawStart[1], jawStart[2], jaw+".scalePivot", jaw+".rotatePivot")
    base.parent(jaw, "CTRL_HEAD")
    base.makeIdentity(jaw, apply = True, t = 1, r = 1, s = 1)    
        
  
 
def CreateFingers(fingerCount):
    sides = ['L', 'R']
    
    for side in sides:
        for i in range(0, fingerCount):
            
            #base.move(fingerPosition[0], fingerPosition[1], fingerPosition[2], fingerGrp)
            #base.makeIdentity(fingerGrp, apply = True, t = 1, r = 1, s = 1) 
            #print fingerRotation
            for j in range(0,3):
                #fingerRotation = base.xform(base.ls("RIG_"+side+"_Finger_"+str(i)+"_"+str(j)), q = True, ws = True, ro = True)
                fingerRotation = base.xform(base.ls("Loc_"+side+"_Finger_"+str(i)+"_"+str(j)), q = True, ws = True, ro = True)
                fingerPosition = base.xform(base.ls("Loc_"+side+"_Finger_"+str(i)+"_"+str(j)), q = True, ws = True, t = True)
            
                allFingers =  base.ls("RIG_"+side+"_Finger_"+str(i)+"_"+str(j))   
        
                finger = base.curve(p =[(0,0,0), (0,0,0.5), (0.2, 0, 0.7),(0,0,0.9), (-0.2, 0, 0.7), (0,0,0.5)], degree = 1, name = "CTRL_"+side+"_Finger_"+str(i)+"_"+str(j))
                base.rotate(-90,0,0, finger)
                           
                #base.parent(finger, fingerGrp)
                for k, fi in enumerate(allFingers):
                    fingerPos = base.xform(fi, q = True, t = True, ws = True)
                    fingerRot = base.joint(fi, q = True, o = True)
                    base.scale(0.1, 0.1, 0.1, finger)    
                    base.move(fingerPos[0], fingerPos[1], fingerPos[2], finger)
                fingerGrp = base.group(em = True, n = "CTRL_GRP_"+side+"_Finger_"+str(i)+"_"+str(j))
                base.move(fingerPosition[0], fingerPosition[1], fingerPosition[2], fingerGrp)
                base.rotate(0, fingerRotation[1], 0, fingerGrp)     
                base.makeIdentity(finger, apply = True, t = 1, r = 1, s = 1)      
                base.makeIdentity(fingerGrp, apply = True, t = 1, r = 1, s = 1)      
                base.parent(finger, fingerGrp)
                base.rotate(0, fingerRotation[1], 0, fingerGrp, r = True)   

                if j > 0:
                    base.parent(fingerGrp, "CTRL_"+side+"_Finger_"+str(i)+"_"+str(j-1))
                else:
                    base.parent(fingerGrp, "CTRL_"+side+"_Wrist")
        
def createFeet():
    l_arrow = base.curve(p = [(1,0,0),(1,0,2), (2,0,2),(0,0,6), (-2,0,2), (-1,0,2), (-1,0,0), (1,0,0)], degree = 1, name = "CTRL_L_Foot")
    base.addAttr(shortName = "KF", longName = "Knee_Twist", attributeType = 'double', defaultValue = 0, minValue = -100, maxValue = 100, keyable = True)            
    base.addAttr(shortName = "KR", longName = "Knee_Fix", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)            
    base.addAttr(shortName = "FR", longName = "Foot_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)            
    base.addAttr(shortName = "BR", longName = "Ball_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)            


    r_arrow = base.curve(p = [(1,0,0),(1,0,2), (2,0,2),(0,0,6), (-2,0,2), (-1,0,2), (-1,0,0), (1,0,0)], degree = 1, name = "CTRL_R_Foot")
    base.addAttr(shortName = "KF", longName = "Knee_Twist", attributeType = 'double', defaultValue = 0, minValue = -100, maxValue = 100, keyable = True)            
    base.addAttr(shortName = "KR", longName = "Knee_Fix", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)            
    base.addAttr(shortName = "FR", longName = "Foot_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True) 
    base.addAttr(shortName = "BR", longName = "Ball_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)                           
  
    
    base.scale(0.08, 0.08, 0.08, l_arrow)
    base.scale(0.08, 0.08, 0.08, r_arrow)
        
    l_footPos = base.xform(base.ls("RIG_L_Foot"), q = True, t = True, ws = True)
    r_footPos = base.xform(base.ls("RIG_R_Foot"), q = True, t = True, ws = True)  
        
    base.move(l_footPos[0], 0, l_footPos[2], l_arrow)
    base.move(r_footPos[0], 0, r_footPos[2], r_arrow)    
    
    base.makeIdentity(l_arrow, apply = True, t = 1, r = 1, s = 1)        
    base.makeIdentity(r_arrow, apply = True, t = 1, r = 1, s = 1) 
        
    base.parent(l_arrow, "Main_CTRL")
    base.parent(r_arrow, "Main_CTRL")    
 
    
        
def setColors():
    base.setAttr('Main_CTRL.overrideEnabled', 1)
    base.setAttr('Main_CTRL.overrideRGBColors', 1)
    base.setAttr('Main_CTRL.overrideColorRGB', 1,1,1)        
     