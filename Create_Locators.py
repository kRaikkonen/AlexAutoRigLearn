import maya.cmds as base









def createLocators(spineValue, fingerValue):
    
    global spineJointCount
    global fingerCount
    
    
    spineJointCount = spineValue
    fingerCount = fingerValue
    
    
    
    
    if base.objExists("Loc_Master"):
        print('Loc_Master already exists')
    else:
        base.group(em=True, name="Loc_Master")

    root = base.spaceLocator(n='Loc_ROOT')
    base.scale(0.1, 0.1, 0.1, root)
    base.move(0, 1.5, 0, root)
    base.parent(root, "Loc_Master")
    
   
    createSpine()
    
def ReturnSpineAmount():
   return spineJointCount
   
def ReturnFingersAmount():
   return fingerCount


def createSpine():
    for i in range(0, spineJointCount):
        spine = base.spaceLocator(n='Loc_SPINE_' + str(i))
        base.scale(0.1, 0.1, 0.1, spine)
        if i == 0:
            base.parent(spine, 'Loc_ROOT')
        else:
            base.parent(spine, 'Loc_SPINE_' + str(i - 1))
        base.move(0, 1.75 + (0.25 * i), 0, spine)
    createHead()
    
    
    createArms(1)
    createArms(-1)
    createLegs(1)
    createLegs(-1)


def createHead():
    neck = base.spaceLocator(n = 'Loc_Neck_Start')
    base.parent(neck, 'Loc_SPINE_' + str(ReturnSpineAmount() - 1))
    base.scale(1,1, 1, neck)
    base.move(0,1.6 + (0.25 * ReturnSpineAmount()), 0, neck) 
    
    neck = base.spaceLocator(n = 'Loc_Neck_End')
    base.parent(neck, 'Loc_Neck_Start')
    base.scale(1,1, 1, neck)
    base.move(0,1.75 + (0.25 * ReturnSpineAmount()), 0, neck) 
    
    
    print (0.25 * ReturnSpineAmount())
    
     
    
    head = base.spaceLocator(n = 'Loc_Head')
    base.parent(head, 'Loc_Neck_End')
    base.scale(1,1,1, head)
    base.move(0, 2 + (0.25 * ReturnSpineAmount()),0, head)  
    
    ## jaw
    jawEnd = base.spaceLocator(n = 'Loc_Jaw_End')
    jawStart = base.spaceLocator(n = 'Loc_Jaw_Start')
    base.parent(jawStart, 'Loc_Head')
    base.parent(jawEnd, jawStart)
    base.scale(1,1,1, jawEnd)
    base.scale(0.5,0.5,0.5, jawStart)
    base.move(0, 1.9 + (0.25 * ReturnSpineAmount()),0.02, jawStart)
    base.move(0, 1.9 + (0.25 * ReturnSpineAmount()),0.15, jawEnd)

    



def createArms(side):
    if side == 1:
        if base.objExists('L_Arm_GRP'):
            print('Left Arm already exists')
        else:
            L_arm = base.group(em=True, name='L_Arm_GRP')
            base.parent(L_arm, 'Loc_SPINE_' + str(ReturnSpineAmount() - 1))
            base.move(0, 1.5 + 0.25 * ReturnSpineAmount(), 0, L_arm)
            
            L_clavicle = base.spaceLocator(n = 'Loc_L_Clavicle')
            base.scale(0.1,0.1,0.1, L_clavicle)
            base.parent(L_clavicle,  L_arm)
            base.move(0.1 * side, 1.5 + (0.25 * ReturnSpineAmount()), 0.1, L_clavicle)
            
            
            #Create L_UpperArm
            L_upperArm = base.spaceLocator( n = 'Loc_L_UpperArm')
            base.scale(0.1,0.1,0.1, L_upperArm)
            base.parent(L_upperArm, L_clavicle)
            base.move(0.35 * side, 1.5 + (0.25 * ReturnSpineAmount()), 0, L_upperArm)
            
            #Create L_Elbow
            L_Elbow = base.spaceLocator( n = 'Loc_L_Elbow')
            base.scale(0.1,0.1,0.1, L_Elbow)
            base.parent(L_Elbow, L_upperArm)
            base.move(0.6 * side, 2, -0.2, L_Elbow)
            
            #Create L_Wrist
            L_Wrist = base.spaceLocator( n = 'Loc_L_Wrist')
            base.scale(0.1,0.1,0.1, L_Wrist)
            base.parent(L_Wrist, L_Elbow)
            
            
            
            
            
            base.move(0.8 * side, 1.5, 0, L_Wrist)
            
            
            createHands(side, L_Wrist)
            
                        
           
            
            

    else:
        if base.objExists('R_Arm_GRP'):
            print('Right Arm already exists')
        else:
            R_arm = base.group(em=True, name='R_Arm_GRP')
            base.parent(R_arm, 'Loc_SPINE_' + str(ReturnSpineAmount() - 1))
            base.move(0, 1.5 + 0.25 * ReturnSpineAmount(), 0, R_arm)
            
            R_clavicle = base.spaceLocator(n = 'Loc_R_Clavicle')
            base.scale(0.1,0.1,0.1, R_clavicle)
            base.parent(R_clavicle, R_arm)
            base.move(0.1 * side, 1.5 + (0.25 * ReturnSpineAmount()), 0.1, R_clavicle)
            
            
            #Create R_UpperArm
            R_upperArm = base.spaceLocator( n = 'Loc_R_UpperArm')
            base.scale(0.1,0.1,0.1, R_upperArm)
            base.parent(R_upperArm, R_clavicle)
            
            #Create R_Elbow
            R_Elbow = base.spaceLocator( n = 'Loc_R_Elbow')
            base.scale(0.1,0.1,0.1, R_Elbow)
            base.parent(R_Elbow, R_upperArm)
            
            #Create R_Wrist
            R_Wrist = base.spaceLocator( n = 'Loc_R_Wrist')
            base.scale(0.1,0.1,0.1, R_Wrist)
            base.parent(R_Wrist, R_Elbow)
            

            #move upper arm
            base.move(0.35 * side, 1.5 + (0.25 * ReturnSpineAmount()), 0, R_upperArm)  
            base.move(0.6 * side, 2, -0.2, R_Elbow)
            base.move(0.8 * side, 1.5, 0, R_Wrist)
            
            createHands(side, R_Wrist)
            

##### Hands #####        
def createHands(side, wrist):
    if side == 1:
        if base.objExists('L_Hand_GRP'):
            print('L_Hand_GRP already exists')
        else:
            hand = base.group(em=True, name='L_Hand_GRP')
            pos = base.xform(wrist, q=True, t=True, ws=True)
            base.move(pos[0], pos[1], pos[2], hand)
            base.parent(hand, 'Loc_L_Wrist')
            for i in range(ReturnFingersAmount()):
                createFingers(1,pos,i)
                
           
                
    else:
        if base.objExists('R_Hand_GRP'):
            print('R_Hand_GRP already exists')
        else:
            hand = base.group(em=True, name='R_Hand_GRP')
            pos = base.xform(wrist, q=True, t=True, ws=True)
            base.move(pos[0], pos[1], pos[2], hand)
            base.parent(hand, 'Loc_R_Wrist')
            for i in range(ReturnFingersAmount()):
                createFingers(-1,pos,i)
                
            
               
    
def createFingers(side, handPos, count):
    
    for x in range(0,4):
        
        if side == 1:
            
            finger = base.spaceLocator(n = 'Loc_L_Finger_' + str(count) + '_' + str(x))
            base.scale(0.05, 0.05, 0.05, finger)
           
            if x == 0:
                base.parent(finger, 'Loc_L_Wrist')
            else:
                
                base.parent(finger, 'Loc_L_Finger_' + str(count) + '_' + str(x - 1))
              
            base.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 *x)), handPos[2] + -(0.05 * count), finger)
        else:        
            finger = base.spaceLocator(n = 'Loc_R_Finger_' + str(count) + '_' + str(x))
            base.scale(0.05, 0.05, 0.05, finger)
            if x == 0:
                base.parent(finger, 'Loc_R_Wrist')
            else:
                base.parent(finger, 'Loc_R_Finger_' + str(count) + '_' + str(x - 1))
            base.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 *x)), handPos[2] + -(0.05 * count), finger)
            
            
            
def createLegs(side):
    if side == 1:
        if base.objExists('Loc_L_Grp'):
            print('Loc_L_Leg already exists')
        else:
            L_upperLegGRP = base.group(em=True, name='L_Leg_GRP')
            base.parent(L_upperLegGRP, 'Loc_ROOT')
            base.move(0.1, 1, 0, L_upperLegGRP)

        L_upperLeg = base.spaceLocator(n='Loc_L_UpperLeg')
        base.scale(0.1, 0.1, 0.1, L_upperLeg)
        base.move(0.15, 1.5, 0, L_upperLeg)
        base.parent(L_upperLeg, 'L_Leg_GRP')
        
        
        ## L knee
        L_Knee = base.spaceLocator(n = 'Loc_L_Knee')
        base.scale(0.1,0.1,0.1, L_Knee)
        base.move(0.15,0.75, 0.05, L_Knee)
        base.parent(L_Knee, 'Loc_L_UpperLeg')
        
        ## L_foot
        L_foot = base.spaceLocator(n = 'Loc_L_Foot')
        base.scale(0.1, 0.1, 0.1, L_foot)
        base.move(0.15, 0.2, 0, L_foot)
        base.parent(L_foot, 'Loc_L_Knee')
        
        ## L_ball
        
        L_ball = base.spaceLocator(n = 'Loc_L_Ball')
        base.scale(0.1,0.1,0.1, L_ball)
        base.move(0.15, 0, 0.15, L_ball)
        base.parent(L_ball, 'Loc_L_Foot')
        
        ## toes
        
        toes = base.spaceLocator(n = 'Loc_L_Toes')
        base.scale(0.1,0.1,0.1, toes)
        base.move(0.15, 0, 0.3, toes)
        base.parent(toes, 'Loc_L_Ball')
        

    else:
        if base.objExists('Loc_R_Grp'):
            print('Loc_R_Leg already exists')
        else:
            R_upperLegGRP = base.group(em=True, name='R_Leg_GRP')
            base.parent(R_upperLegGRP, 'Loc_ROOT')
            base.move(-0.1, 1, 0, R_upperLegGRP)

        R_upperLeg = base.spaceLocator(n='Loc_R_UpperLeg')
        base.scale(0.1, 0.1, 0.1, R_upperLeg)
        base.move(-0.15, 1.5, 0, R_upperLeg)
        base.parent(R_upperLeg, 'R_Leg_GRP')
        
        
        
         ## Knee
        R_Knee = base.spaceLocator(n = 'Loc_R_Knee')
        base.scale(0.1,0.1,0.1, R_Knee)
        base.move(-0.15,0.75, 0.05, R_Knee)
        base.parent(R_Knee, 'Loc_R_UpperLeg')
        
        ## R_foot
        R_foot = base.spaceLocator(n = 'Loc_R_Foot')
        base.scale(0.1, 0.1, 0.1, R_foot)
        base.move(-0.15, 0.2, 0, R_foot)
        base.parent(R_foot, 'Loc_R_Knee')
        
        ## R_ball
        
        R_ball = base.spaceLocator(n = 'Loc_R_Ball')
        base.scale(0.1,0.1,0.1, R_ball)
        base.move(-0.15, 0, 0.15, R_ball)
        base.parent(R_ball, 'Loc_R_Foot')
        
        ## toes
        
        toes = base.spaceLocator(n = 'Loc_R_Toes')
        base.scale(0.1,0.1,0.1, toes)
        base.move(-0.15, 0, 0.3, toes)
        base.parent(toes, 'Loc_R_Ball')


def setColor4Loc():
    base.setAttr('Loc_Master.overrideEnable',1)
    base.setAttr('Loc_Master.overrideRGBColors',1)

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
